// 챔피언 목록 포지션별 표시

function showChampions(position) {
    // 챔피언 목록 초기화
    document.getElementById("championsList").innerHTML = "";

    // 선택한 포지션에 따라 챔피언을 표시
    if (position === "top") {
    } else if (position === "jungle") {
    } else if (position === "mid") {
    } else if (position === "adc") {
    } else if (position === "spt") {
    }
}

// 데이터의 일부만 작성해도 해당 데이터가 포함 된 모든 요소 표시

function searchChampions() {
    // 검색 상자에서 입력된 텍스트 가져오기
    const searchText = document.getElementById("championsSearch").value.toLowerCase();

    // 챔피언 데이터 (예: JSON 객체로 정의된 데이터)를 가져오거나, 서버에서 검색을 수행합니다.

    // 검색 결과를 표시할 요소 가져오기
    const championPortraits = document.getElementById("championPortraits");

    // 검색 결과 초기화
    championPortraits.innerHTML = "";

    // 검색된 챔피언 목록을 필터링하고 표시
    const filteredChampions = championData.filter((champion) => {
        return champion.name.toLowerCase().includes(searchText);
    });

    // 검색 결과를 HTML로 생성하여 표시
    for (const champion of filteredChampions) {
        const championElement = document.createElement("div");
        championElement.textContent = champion.name;
        championPortraits.appendChild(championElement);
    }
}

// input이 클릭되었을 때 엔터키로 검색 가능

function searchOnEnter(event) {
    if (event.key === "Enter") {
        searchChampions(); // Enter 키가 눌렸을 때 검색 기능 호출
    }
}
