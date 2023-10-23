document.addEventListener("DOMContentLoaded", function () {
    var ladderUrl = "{% static 'leaderboards/type_ladder.html' %}";
    var ladderFlexUrl = "{% static 'leaderboards/type_ladder_flex.html' %}";
    var championsUrl = "{% static 'leaderboards/type_champions.html' %}";
    var levelUrl = "{% static 'leaderboards/type_level.html' %}";

    function showType(type) {
        var url;
        if (type === "type_ladder") {
            url = ladderUrl;
        } else if (type === "type_ladder_flex") {
            url = ladderFlexUrl;
        } else if (type === "type_champions") {
            url = championsUrl;
        } else if (type === "type_level") {
            url = levelUrl;
        } else {
            url = ladderUrl;
        }

        if (url) {
            fetch(url)
                .then(function (response) {
                    return response.text();
                })
                .then(function (html) {
                    document.querySelector(".summoners_info_display").innerHTML = html;
                })
                .catch(function (error) {
                    console.error(error);
                });
        }
    }

    // 페이지 로딩 시 기본으로 특정 타입을 표시할 수 있습니다.
    showType("type_ladder");

    // 버튼 클릭 이벤트에 따라 타입 변경
    var buttons = document.querySelectorAll(".type_btn button");
    buttons.forEach(function (button) {
        button.addEventListener("click", function () {
            var type = button.getAttribute("data-type");
            showType(type);
        });
    });
});

// input이 클릭되었을 때 엔터키로 검색 기능

function searchOnEnter(event) {
    if (event.key === "Enter") {
        searchChampions(); // Enter 키가 눌렸을 때 검색 기능 호출
    }
}
