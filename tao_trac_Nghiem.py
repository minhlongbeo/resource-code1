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
        <button type="button" onclick="if (number != 0) {answertext.innerText+=number} else {answertext.innerText+=(old_index+number)}">=</button>
    </div>

    <div class="customgui">
        <button type="button" onclick="CheckNumber(7)">7</button>
        <button type="button" onclick="CheckNumber(8)">8</button>
        <button type="button" onclick="CheckNumber(9)">9</button>
        <button type="button" onclick="labeltext.innerText=''; answertext.innerText='='; number=0; old_number=0; old_index=0; current_calculator='+';">X</button>
    </div>

    <p id="ShowNumber" style="border: 2px solid black; display: inline-block;"></p>
    <p id="ShowAnswer" style="border: 2px solid black; display: inline-block;">=</p>

    <script>
        const labeltext = document.getElementById("ShowNumber");
        const answertext = document.getElementById("ShowAnswer");

        let old_index = 0;
        let old_number = 0;
        let number = 0;

        const data_calculator = {
            "+" : function(a) {number += old_number + a;},
            "-" : function(a) {number -= a;},
            "*" : function(a) {number += old_number * a;},
            "/" : function(a) {number = old_number / a;},
        };
        let current_calculator = "+";

        function CheckNumber(num) {
            if (num > -1) {
                if (old_index > -1) {
                    labeltext.innerText+=''
                    old_number = (old_number*10) + num;
                } else {
                    data_calculator[current_calculator](num);
                };
            } else {
                current_calculator = num;
            }
            
            old_index = num;
            labeltext.innerText+=num;
        };
    </script>
</body>
