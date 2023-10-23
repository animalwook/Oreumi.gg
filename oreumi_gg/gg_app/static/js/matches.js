
const currentURL = window.location.href;
const url = new URL(currentURL);
const spliturl = url.pathname.split('/');
const country = spliturl[2];
const summonerName = decodeURIComponent(spliturl[3]);



function addmatch(count) {
    fetch(`/api/summoners_info/${country}/${summonerName}/${count}`)
        .then(response => response.json())
        .then(data => {
            // 데이터 사용
            console.log(data);
            display(data);
        })
        .catch(error => {
            console.log(error);
            console.log(error.stack);
            console.log(error.message);
            console.error("API 호출 중 오류 발생:", error);
        });
}

function display(data) {
    const matchDataContainer = document.getElementById("addmatch");
    const total_matchcount = document.getElementById("total_matchcount");
    const total_wincount = document.getElementById("total_wincount");
    const total_losecount = document.getElementById("total_losecount");
    const total_winrate = document.getElementById("total_winrate")
    const total_kill = document.getElementById("total_kill")
    const total_death = document.getElementById("total_death")
    const total_assist = document.getElementById("total_assist")
    const total_kda = document.getElementById("total_kda")
    const total_killpart = document.getElementById("total_killpart")
    const matches = data.matches;

    let html = '';
    matches.forEach(match => {
        let itemsHTML = '';
        let champHTML = '';
        match.search_player_item.forEach(item => {
            if (item != 0) {
                itemsHTML += `<img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/item/${ item }.png" style="width: 100px; height: 100px;">`;
                }
            });
        for (let i = 1; i <= 10; i++) {
            if (Array.isArray(match[i])) {
                match[i].forEach(item => {
                    if (i <= 5) {
                        champHTML += `
                        <li style="list-style-type: none;">
                        <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/champion/${item.championname}.png">
                        ${item.summonername}
                        </li>
                    `;
                    }
                    else if (i <= 10) {
                    if (item.championname) {
                        champHTML += `
                        <li style="list-style-type: none;">
                        <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/champion/${item.championname}.png">
                        ${item.summonername}
                        </li>
                    `; 
                    }
                }
                        
                });
            }
        }
        html += `
      <div style="border: 2px solid #333; display: flex;">
          <div class="match_info">
              <li style="list-style-type: none;"> ${match.win_or_not} </li>
              <li style="list-style-type: none;"> ${match.game_type} </li>
              <li style="list-style-type: none;"> ${match.game_playtime}</li>
              <li style="list-style-type: none;"> ${match.game_time}</li>
          </div>
          <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/champion/${match.search_player_champ}.png" style="width:160px; height:160px;">
          <p>${match.search_player_champlevel}</p>
          <div class="champ_spell">
              <li style="list-style-type: none;"><img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/spell/${match.search_player_summonerspell1}.png"></li>
              <li style="list-style-type: none;"><img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/spell/${match.search_player_summonerspell2}.png"></li>
          </div>
          <div class="rune">
              <li style="list-style-type: none;"><img src="https://ddragon.canisback.com/img/${match.search_player_main_rune}" style="width: 80px; height: 80px;"></li>
              <li style="list-style-type: none;"><img src="https://ddragon.canisback.com/img/perk-images/Styles/${match.search_player_sub_rune}.png"></li>
          </div>
          <div class="kill">
              <li style="list-style-type: none;"><p> ${match.search_player_kill} / ${match.search_player_death} / ${match.search_player_assist}</p></li>
              <li style="list-style-type: none;"><p>kda ${match.search_player_kda}</p></li>
          </div>
          <div class="total">
              <li style="list-style-type: none;">
                  <p>킬관여율 ${match.search_player_killpart}% </p>
                  <p>CS ${match.search_player_totalminions_kill} (${match.search_player_minperminions})</p>
                  <p>제어 와드 ${match.search_player_visionWardsBoughtInGame}</p>
              </li>
          </div>
          ${itemsHTML}
          ${champHTML}
        </div>
        `;
  });
    
    matchDataContainer.innerHTML += html;
    total_matchcount.innerHTML = `${count}전`
    let winCount = parseInt(total_wincount.textContent) + data.total_calculate.win_count;
    let loseCount = parseInt(total_losecount.textContent) + data.total_calculate.lose_count;
    let winRate = (winCount / (winCount + loseCount)).toFixed(2) * 100;
    let killCount = parseFloat(total_kill.textContent) + data.total_calculate.total_kill;
    let assistCount = parseFloat(total_assist.textContent) + data.total_calculate.total_assist;
    let deathCount = parseFloat(total_death.textContent) + data.total_calculate.total_death;
    let kda = parseFloat(total_kda.textContent.split(":")[0]) + data.total_calculate.total_kda;
    let killPart = parseInt(total_killpart.textContent) + data.total_calculate.total_kill_part;

    total_wincount.textContent = winCount + "승";
    total_losecount.textContent = loseCount + "패";
    total_winrate.textContent = winRate + "%";
    total_kill.textContent = (killCount / 2).toFixed(1);
    total_death.textContent = (deathCount / 2).toFixed(1);
    total_assist.textContent = (assistCount / 2).toFixed(1);
    total_kda.textContent = (kda / 2).toFixed(2) + ":1";
    total_killpart.textContent = (killPart / 2).toFixed(0) + "%";
}
let count = 20;
const fetchButton = document.getElementById('addmatch_btn');
fetchButton.addEventListener('click', function() {
    addmatch(count)
    count += 20;
});