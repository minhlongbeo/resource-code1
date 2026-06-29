<head>
    <style>
        .customgui {margin-bottom: 10px; display : flex; gap: 10px; }
        button {padding: 10px 15px; cursor: pointer;}
    </style>
</head>
<body>
    <h1>Máy tính test</h1>

    <div class="customgui">
        <button type="button" onclick="CheckNumber('+')">+</button>
        <button type="button" onclick="CheckNumber('-')">-</button>
        <button type="button" onclick="CheckNumber('*')">*</button>
        <button type="button" onclick="CheckNumber('/')">/</button>
        <button type="button" onclick="PreMove()"> <- </button>
    </div>

    <div class="customgui">
        <button type="button" onclick="CheckNumber(0)">0</button>
        <button type="button" onclick="CheckNumber(1)">1</button>
        <button type="button" onclick="CheckNumber(2)">2</button>
        <button type="button" onclick="CheckNumber(3)">3</button>
        <button type="button" onclick="Start_Bracket('Base_level')"> ( </button>
    </div>

    <div class="customgui">
        <button type="button" onclick="CheckNumber(4)">4</button>
        <button type="button" onclick="CheckNumber(5)">5</button>
        <button type="button" onclick="CheckNumber(6)">6</button>
        <button type="button" onclick="ShowCase()">=</button>
        <button type="button" onclick="End_Bracket()"> ) </button>
    </div>

    <div class="customgui">
        <button type="button" onclick="CheckNumber(7)">7</button>
        <button type="button" onclick="CheckNumber(8)">8</button>
        <button type="button" onclick="CheckNumber(9)">9</button>
        <button type="button" onclick="ResetCalculator()">X</button>
        <button type="button" onclick="console.log('Đã bảo đừng nhấn rồi mà')"> Đừng nhấn </button>
    </div>

    <p id="ShowNumber" style="border: 2px solid black; display: inline-block; min-width: 50px; min-height: 20px;"></p>
    <p id="ShowAnswer" style="border: 2px solid black; display: inline-block;">=</p>

    <script>
        const labeltext = document.getElementById("ShowNumber");
        const answertext = document.getElementById("ShowAnswer");
        
        let old_number = 0;
        let current_number = 0;
        let number = 0;

        let data_number = [0, 0];
        let calculator_box_number = [];
        let current_data_number = data_number;

        let start_bracket = [];
        let multiplier_bracket = [];

        const data_calculator = {
            "+" : function(a, b) { return a + b; },
            "-" : function(a, b) { return a - b; },
            "*" : function(a, b) { return a * b; },
            "/" : function(a, b) { return a / b; }
        };

        const check_same_sign = {
            "+" : true,
            "-" : true,
        };

        const check_first_part = {
            "+" : true,
            "*" : true,
            "/" : true,
            ")" : true
        }

        const check_last_part = {
            "+" : true,
            "*" : true,
            "/" : true,
            "(" : true
        }

        const check_sign_to_calculator = {
            "Multiplier_level" : 0
        }

        function CheckNumber(num) {
            if (num > -1) {
                current_number = (current_number * 10) + num;
            } else {
                old_number = current_number;
                current_number = 0;

                if (check_same_sign[num] && multiplier_bracket.length > 0) {
                    multiplier_bracket.pop();

                    End_Bracket();
                } else if (multiplier_bracket.length == 0) {
                    Start_Bracket('Multiplier_level');

                    multiplier_bracket.push(true);
                };

                if (typeof current_data_number[current_data_number.length - 1] !== "string") {
                    current_data_number.push(old_number);
                };

                current_data_number.push(num);
            };

            labeltext.innerText += num;
        };

        function Check_spelling(now_data) {
            let lastpoint = now_data[now_data.length - 1];

            if (start_bracket.length > 0) {
                for (i = 0; i < start_bracket.length; i++) {
                    End_Bracket();
                }
            }

            if (current_number !== 0) {
                now_data.push(current_number);
                lastpoint = current_number;
            };

            if (check_first_part[now_data[2]]) {
                now_data.splice(2, 1);
            };

            if (check_last_part[lastpoint]) {
                labeltext.innerText = labeltext.innerText.slice(0, labeltext.innerText.length-1) ;
            };
        };

        function Calculator_Base(Data_Array, type_calculator) {
            let new_number = 0;
            let new_calculator = "+";

            if (check_sign_to_calculator[type_calculator]) {
                new_number = check_sign_to_calculator[type_calculator];
            };

            for (let i = 2; i < Data_Array.length; i++) {
                let test = Data_Array[i];

                if (typeof test === "number") { 
                    new_number = data_calculator[new_calculator](new_number, test);
                } else {
                    new_calculator = test;
                };
            };
            
            return new_number;
        };

        function ShowCase() {
            Check_spelling(data_number);

            let lens = current_data_number.length;
            let lens_box_calculator = calculator_box_number.length;
            let old_number_box = [];

            for (let i = lens_box_calculator - 1; i >= 0; i--) {
                let current_test = calculator_box_number[i];
                let data_get_pointed = current_test[1];
                let index_pointed = current_test[0];

                data_get_pointed[index_pointed] = Calculator_Base(current_test, data_get_pointed[index_pointed]);
            };

            number = Calculator_Base(data_number, undefined);

            answertext.innerText = "= " + number;
        };

        function Start_Bracket(calculator_type) {
            if (current_number !== 0) {
                CheckNumber("*");
            };

            console.log(calculator_type);

            start_bracket.push(true);
            
            data_number.push(calculator_type); 
            current_data_number = [data_number.length-1, current_data_number];
            calculator_box_number[calculator_box_number.length] = current_data_number;
        };

        function End_Bracket() {
            let length_check = start_bracket.length;

            if (current_number !== 0) {
                current_data_number.push(current_number);
            };

            if (typeof current_data_number[current_data_number.length - 1] === "string") {
                current_data_number.push(old_number);
            };

            if (length_check < 1) {return};
            
            if (length_check == 1) {
                current_data_number = data_number;
            } else {
                current_data_number = calculator_box_number[length_check - 2]
            };

            start_bracket.pop();
        };

        function ResetCalculator() {
            labeltext.innerText = "";
            answertext.innerText = "";

            old_number = 0;
            current_number = 0;
            number = 0;

            data_number = [0, 0];
            calculator_box_number = [];
            current_data_number = data_number;

            start_bracket = [];
            multiplier_bracket = [];
        };

        function PreMove() {
            let current_text = labeltext.innerText;

            if (current_number == 0) {
                let last_number = current_data_number[data_number.length - 2];

                if (last_number > -1) {
                    current_number = last_number;
                    
                    current_data_number.pop();
                };

                current_data_number.pop();
            } else {
                current_number = Math.floor(current_number/10);
            };

            labeltext.innerText = current_text.slice(0, current_text.length - 1);
        };
    </script>
</body>
