document.addEventListener("DOMContentLoaded", function () {
    const article = document.querySelector(".match_container");
    const node2 = document.querySelector(".node2");

    // article의 높이를 가져와서 높이에서 일부 영역을 뺀 값을 .node2의 마진 바텀으로 설정
    const articleHeight = article.clientHeight;
    const marginHeight = articleHeight - 300;
    node2.style.marginBottom = marginHeight + "px";
});
