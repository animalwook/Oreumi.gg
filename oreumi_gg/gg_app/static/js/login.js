document.addEventListener("DOMContentLoaded", function () {
    let modal = document.getElementById("login"); // 모달
    let modalBackground = document.getElementById("modal-background"); // 모달 백그라운드
    let loginButton = document.querySelector(".auth_link"); // 로그인 버튼

    // 로그인 버튼 클릭 시 모달과 백그라운드 표시
    loginButton.addEventListener("click", function () {
        modal.style.display = "block";
        modalBackground.style.display = "block";
        modalBackground.removeEventListener("click", modalBackgroundClickHandler);
    });

    // 모달 백그라운드 클릭 시 모달 숨김
    modalBackground.addEventListener("click", function () {
        modal.style.display = "none";
        modalBackground.style.display = "none";
        modalBackground.addEventListener("click", modalBackgroundClickHandler);
    });
});
