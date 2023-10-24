$(document).ready(function () {
    // 모달 열기 버튼에 대한 클릭 이벤트 처리
    $("#openLoginModal").on("click", function () {
        // 모달과 모달 배경 모두 표시
        $("#login").modal("show");
        $("#modal-background").show();
    });

    // 모달 닫기 버튼에 대한 클릭 이벤트 처리
    $("#closeLoginModal").on("click", function () {
        // 모달과 모달 배경 모두 숨김
        $("#login").modal("hide");
        $("#modal-background").hide();
    });
});
