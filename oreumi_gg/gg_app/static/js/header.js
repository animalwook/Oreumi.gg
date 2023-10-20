// input이 클릭되었을 때 엔터키로 검색 기능

function searchOnEnter(event) {
    if (event.key === "Enter") {
        searchChampions(); // Enter 키가 눌렸을 때 검색 기능 호출
    }
}
