const buttons = document.querySelectorAll('.game-type button');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            // 현재 선택된 버튼의 값
            const original_btn = document.querySelector('.selected');
            const li = button.parentElement;
            if (li.classList.contains("notselected")) {
                original_btn.classList.remove('selected');
                original_btn.classList.add('notselected');
                li.classList.add("selected");
                li.classList.remove("notselected");
            }
        });
    });