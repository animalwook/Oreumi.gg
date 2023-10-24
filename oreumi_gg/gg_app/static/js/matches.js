
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
        let bluechampHTML = '';
        let redchampHTML = '';
        let detailHTML = '';

        if (match.win_or_not_eng == "defeat") {
            detailHTML += `<img src="https://s-lol-web.op.gg/images/icon/icon-arrow-down-red.svg?v=1697786050877" width="24" alt="More" height="24">`;
        }
        else if (match.win_or_not_eng == "repeat") {
            detailHTML += `<img src="https://s-lol-web.op.gg/images/icon/icon-arrow-down.svg?v=1697786050877" width="24" alt="More" height="24">`;
        }
        else {
            detailHTML += `<img src="https://s-lol-web.op.gg/images/icon/icon-arrow-down-blue.svg?v=1697786050877" width="24" alt="More" height="24">`;
        }



        match.search_player_item.forEach(item => {
            if (item != 0) {
                itemsHTML += `
                <li style="list-style-type: none;">
                    <div class style="position: relative">
                        <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/item/${ item }.png" width="22" height="22">
                    </div>
                </li>
                `;
                }
            });
        for (let i = 1; i <= 10; i++) {
            if (Array.isArray(match[i])) {
                match[i].forEach(item => {
                    if (i <= 5) {
                        bluechampHTML += `
                        <li class="team" style="list-style-type: none;">
                            <div class="team_icon" style="position: relative">
                                <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/champion/${item.championname}.png" width="16" height="16">
                            </div>
                            <div class="name">
                                <a href="/summoners/kr/${item.summonername}" rel="noreferrer">
                                    ${item.summonername}
                                </a>
                            </div>
                        </li>
                    `;
                    }
                    else if (i <= 10) {
                        if (item.championname) {
                            redchampHTML += `
                            <li class="team" style="list-style-type: none;">
                                <div class="team_icon" style="position: relative">
                                    <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/champion/${item.championname}.png" width="16" height="16">
                                </div>
                                <div class="name">
                                    <a href="/summoners/kr/${item.summonername}" rel="noreferrer">
                                        ${item.summonername}
                                    </a>
                                </div>
                            </li>
                        `; 
                        }
                    }
                });
            }
        }
        html += `
        <li class="game-item">
          <div result="${match.win_or_not_eng}" class="game-match result">
            <div class="content">
                <div class="game-content">
                    <div class="game">
                        <div class="type">${match.game_type}</div>
                        <div class="time-stamp">
                            <div class style="position: relative;">${match.game_time}</div>
                        </div>
                        <div class="result">${match.win_or_not}</div>
                        <div class="length">${match.game_playtime}</div>
                    </div>
                    <div class="info">
                        <div>
                            <div class="champion">
                                <div class="icon">
                                    <a href="" rel="noreferrer">
                                        <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/champion/${match.search_player_champ}.png" width="48" height="48">
                                        <span class="champion-level">${match.search_player_champlevel}</span>
                                    </a>
                                </div>
                                <div class="spells">
                                    <div class="spell">
                                        <div class style="position: relative;">
                                            <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/spell/${match.search_player_summonerspell1}.png" width="22" height="22">
                                        </div>
                                    </div>
                                    <div class="spell">
                                        <div class style="position: relative;">
                                            <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/spell/${match.search_player_summonerspell2}.png" width="22" height="22">
                                        </div>
                                    </div>
                                </div>
                                <div class="runes">
                                    <div class="rune">
                                        <div class style="position: relative;">
                                            <img src="https://ddragon.canisback.com/img/${match.search_player_main_rune}" width="22" height="22">
                                        </div>
                                    </div>
                                    <div class="rune">
                                        <div class style="position: relative;">
                                            <img src="https://ddragon.canisback.com/img/perk-images/Styles/${match.search_player_sub_rune}.png" width="22" height="22">
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="kill_death_assist">
                                <div class="k-d-a">
                                    <span>${match.search_player_kill}</span>
                                    <span> / </span>
                                    <span class="d">${match.search_player_death}</span>
                                    <span> / </span>
                                    <span>${match.search_player_assist}</span>
                                </div>
                                <div class="ratio">
                                    <span>${match.search_player_kda}:1</span>
                                </div>
                            </div>
                            <div class="stats">
                                <div class="p-kill">
                                    <div class style="position: relative;">
                                        킬관여 ${match.search_player_killpart}%
                                    </div>
                                </div>
                                <div class="controlward">제어 와드 ${match.search_player_visionWardsBoughtInGame}</div>
                                <div class="cs">
                                    <div class style="position: relative;">
                                        CS ${match.search_player_totalminions_kill} (${match.search_player_minperminions})
                                    </div>
                                </div>
                                <div class="average-tier"><div class style="position relative;"></div></div>
                            </div>
                        </div>
                        <div>
                            <div class="items">
                                <ul>
                                    ${itemsHTML}
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="participants">
                        <ul>
                            ${bluechampHTML}
                        </ul>
                        <ul>
                            ${redchampHTML}
                        </ul>
                    </div>
                </div>
            </div>
            <div class="action">
                <button class="detail" data-match-info="${JSON.stringify(match)}" match-result="${match.win_or_not_eng}" status="open">
                    ${detailHTML}
                </button>
            </div>
          </div>
        </li>
        `;
  });
    
    matchDataContainer.insertAdjacentHTML('afterend', html);
    total_matchcount.textContent = `${count}전`
    let winCount = parseInt(total_wincount.textContent) + data.total_calculate.win_count;
    let loseCount = parseInt(total_losecount.textContent) + data.total_calculate.lose_count;
    let winRate = (winCount / (winCount + loseCount)).toFixed(2) * 100;
    let killCount = parseFloat(total_kill.textContent) + data.total_calculate.total_kill;
    let assistCount = parseFloat(total_assist.textContent) + data.total_calculate.total_assist;
    let deathCount = parseFloat(total_death.textContent) + data.total_calculate.total_death;
    let kda = parseFloat(total_kda.textContent.split(":")[0]) + data.total_calculate.total_kda;
    let killPart = parseInt((total_killpart.textContent).split(" ")[1]) + data.total_calculate.total_kill_part;
    total_wincount.textContent = winCount + "승";
    total_losecount.textContent = loseCount + "패";
    total_winrate.textContent = winRate + "%";
    total_kill.textContent = (killCount / 2).toFixed(1);
    total_death.textContent = (deathCount / 2).toFixed(1);
    total_assist.textContent = (assistCount / 2).toFixed(1);
    total_kda.textContent = (kda / 2).toFixed(2) + ":1";
    total_killpart.textContent = "킬관여 " + (killPart / 2).toFixed(0) + "%";
}
let count = 20;
const fetchButton = document.getElementById('addmatch_btn');
fetchButton.addEventListener('click', function() {
    addmatch(count)
    count += 20;
});