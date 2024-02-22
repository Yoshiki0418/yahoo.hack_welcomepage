// // モーダルを開く関数
// function openModal() {
//   document.getElementById('myModal').style.display = "block";
// }

// // モーダルを閉じる関数
// function closeModal() {
//   document.getElementById('myModal').style.display = "none";
// }


//クローゼット収納用モーダルウィンドウ
// モーダルを開く関数
function openModal_closet() {
  document.getElementById('closetModal').style.display = "block";
}

// モーダルを閉じる関数
function closeModal_closet() {
  document.getElementById('closetModal').style.display = "none";
}

// ページ読み込み時にイベントリスナーを設定
window.onload = function() {
  // // モーダル1のイベントリスナーを設定
  // document.getElementById('myBtn').addEventListener('click', openModal);
  // document.getElementsByClassName('close')[0].addEventListener('click', closeModal);
  // window.onclick = function(event) {
  //   if (event.target == document.getElementById('myModal')) {
  //     closeModal();
  //   }
  // }

  // モーダル2のイベントリスナーを設定
  document.getElementById('closetBtn1').addEventListener('click', openModal_closet);
  document.getElementById('closetBtn2').addEventListener('click', openModal_closet);
  document.getElementById('closetBtn3').addEventListener('click', openModal_closet);
  document.getElementById('closetBtn4').addEventListener('click', openModal_closet);
  document.getElementById('closetBtn5').addEventListener('click', openModal_closet);
  document.getElementsByClassName('close')[1].addEventListener('click', closeModal_closet);
  // window.onclick イベントは1つの関数にまとめて設定する
  window.onclick = function(event) {
    if (event.target == document.getElementById('myModal')) {
      closeModal();
    }
    if (event.target == document.getElementById('closetModal')) {
      closeModal_closet();
    }
  };
};
