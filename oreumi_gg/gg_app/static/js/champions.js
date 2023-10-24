// 챔피언 목록 포지션별 표시

function showChampions(position) {
    // 챔피언 목록 초기화
    // document.getElementById("championsList").innerHTML = "";
    var newUrl = 'champions_tier/' + position + '/';
    window.location.href = newUrl;
    // 선택한 포지션에 따라 챔피언을 표시
    // if (position === "top") {

    // } else if (position === "jungle") {
    // } else if (position === "mid") {
    // } else if (position === "adc") {
    // } else if (position === "spt") {
    // }
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

//지역 드롭다운 박스 변경 감지
// document.getElementById("region-select").addEventListener("change", function() {
//     // 선택된 포지션 가져오기
//     var selectedPosition = document.getElementById("region-select").value;
    
//     // Django URL 생성
//     var url = "{% url 'gg_app:champion_tier' region='%s' %}".replace('%s', selectedPosition);
    
//     // 페이지 이동 (드롭다운 목록 변경과 함께)
//     document.getElementById("champion-tier-link").href = url;
//     document.getElementById("champion-tier-link").click();
//   });

const tabButtons = document.querySelectorAll(".champions_tab");
const STORAGE_KEY = "selected_tab";
const regionSelect = document.getElementById("region-select");
const tierSelect = document.getElementById("tier-select");
const REGION_STORAGE_KEY = "selected_region";
const TIER_STORAGE_KEY = "selected_tier";

tabButtons.forEach((button) => {
  button.addEventListener("click", function (event) {
    event.stopPropagation();
    // 선택된 탭의 클래스 변경
    tabButtons.forEach((btn) => {
      btn.classList.remove("active");
    });
    button.classList.add("active");


    const selectedPosition = button.getAttribute("data-position");
    localStorage.setItem(STORAGE_KEY, selectedPosition);

    // URL 업데이트
    updateURL();
  });
});

// 드롭다운 박스의 변경 이벤트에 대한 핸들러
regionSelect.addEventListener("change", function () {
    const selectedRegion = regionSelect.value;
    localStorage.setItem(REGION_STORAGE_KEY, selectedRegion);
});

tierSelect.addEventListener("change", function () {
    const selectedTier = tierSelect.value;
    localStorage.setItem(TIER_STORAGE_KEY, selectedTier);
});

//탭 유지를 위한 로드할때 탭상태 불러오기
window.addEventListener("load", function () {
    const selectedTab = localStorage.getItem(STORAGE_KEY);
    if (selectedTab) {
      const buttonToActivate = document.querySelector(`.champions_tab[data-position='${selectedTab}']`);
      if (buttonToActivate) {
        buttonToActivate.classList.add("active");
      }
    }
    
    const savedRegion = localStorage.getItem(REGION_STORAGE_KEY);
    if (savedRegion) {
        regionSelect.value = savedRegion;
    }

    const savedTier = localStorage.getItem(TIER_STORAGE_KEY);
    if (savedTier) {
        tierSelect.value = savedTier;
    }

  });

  function updateURL() {
    //탭유지를 위한 변수 저장
    const selectedPosition = document.querySelector(".champions_tab.active").getAttribute("data-position");
    const selectedRegion = regionSelect.value;
    const selectedTier = tierSelect.value;
  
    // URL을 동적으로 생성
    const url = `/champions/champions_tier/${selectedPosition}/${selectedRegion}/${selectedTier}`;
    window.location.href = url;
  }