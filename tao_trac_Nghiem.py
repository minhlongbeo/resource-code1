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
    </div>

    <div class="customgui">
        <button type="button" onclick="CheckNumber(4)">4</button>
        <button type="button" onclick="CheckNumber(5)">5</button>
        <button type="button" onclick="CheckNumber(6)">6</button>
        <button type="button" onclick="ShowCase()">=</button>
    </div>

    <div class="customgui">
        <button type="button" onclick="CheckNumber(7)">7</button>
        <button type="button" onclick="CheckNumber(8)">8</button>
        <button type="button" onclick="CheckNumber(9)">9</button>
        <button type="button" onclick="ResetCalculator()">X</button>
    </div>

    <p id="ShowNumber" style="border: 2px solid black; display: inline-block; min-width: 50px; min-height: 20px;"></p>
    <p id="ShowAnswer" style="border: 2px solid black; display: inline-block;">=</p>

    <script>
        const labeltext = document.getElementById("ShowNumber");
        const answertext = document.getElementById("ShowAnswer");
        
        let current_number = 0;
        let number = 0;
        let data_number = [];

        const data_calculator = {
            "+" : function(a) { number += a; },
            "-" : function(a) { number -= a; },
        };

        const final_data_calculator = {
            "+" : true,
            "-" : true,
            undefined : true,
        };

        const second_final = {
            "*" : function(a, b) { return a * b; },
            "/" : function(a, b) { return a / b; },
        };

        let current_calculator = "+";

        function CheckNumber(num) {
            if (num > -1) {
                current_number = (current_number * 10) + num;
            } else {
                data_number.push(current_number);
                data_number.push(num);
                current_number = 0;
            };
            labeltext.innerText += num;
        };

        function ShowCase() {
            data_number.push(current_number);

            if (typeof data_number[0] === 'string') {
                data_number.shift();
            };
            if (typeof data_number[data_number.length - 1] === 'string') {
                data_number.pop();
            };

            let lens = data_number.length;
            let old_number_box = [];
            current_calculator = "+";
            number = 0;

            for (let i = 0; i < lens; i++) {
                let test = data_number[i];

                if (test > -1) { 
                    let future_point = data_number[i + 1];

                    if (final_data_calculator[future_point]) {
                        if (old_number_box.length > 0) {
                            old_number_box.push(test); 

                            let second_number = old_number_box[0];

                            for (let v = 2; v < old_number_box.length; v += 2) {
                                second_number = second_final[old_number_box[v - 1]](second_number, old_number_box[v]);
                            };

                            data_calculator[current_calculator](second_number);
                            old_number_box.length = 0;
                        } else {
                            data_calculator[current_calculator](test);
                        };
                    } else {
                        old_number_box.push(test);
                    };
                } else {
                    if (final_data_calculator[test]) {
                        current_calculator = test;
                    } else {
                        old_number_box.push(test)
                    };
                };
            };

            answertext.innerText = "= " + number;
        };

        function ResetCalculator() {
            labeltext.innerText = ''; 
            answertext.innerText = '='; 
            number = 0; 
            current_number = 0; 
            data_number.length = 0; 
        };

        function PreMove() {
            let current_text = labeltext.innerText;

            if (current_number == 0) {
                let last_number = data_number[data_number.length - 2];

                if (last_number > -1) {
                    console.log("trigger đã xóa đi số cũ (hay nói cách khác là số trong bảng dữ liệu)", last_number);
                    current_number = last_number;
                    
                    data_number.pop();
                };

                data_number.pop();
            } else {
                current_number = Math.floor(current_number/10);
            };

            console.log(data_number);

            labeltext.innerText = current_text.slice(0, current_text.length - 1);
        };
    </script>
</body>
