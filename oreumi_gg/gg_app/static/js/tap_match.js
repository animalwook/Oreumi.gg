const totalmatch = document.querySelector(".match_statics");
const match_20_info = document.querySelector(".match_20");

function changematch(queue) {
    /**
     * api를 사용해서 추가로 20경기를 불러오는 함수
     * @param {int} count
     * @param {int} queue 
     * @return {dict}
     * 
     */
    fetch(`/api/summoners_info/${country}/${summonerName}/${0}/${queue}`)
        .then(response => response.json())
        .then(data => {
            // 데이터 사용
            console.log(data);
            changematch_display(data);
        })
        .catch(error => {
            console.log(error);
            console.log(error.stack);
            console.log(error.message);
            console.error("API 호출 중 오류 발생:", error);
        });
}

function changematch_display(data) {
    
    let totalHTML = '';
    let matchHTML = '';
    const matches = data.matches;
   
    totalHTML += `
        <div id="win_lose">
            <span id="total_matchcount">${data.total_calculate.total_match_count}전</span>
            <span id="total_wincount">${data.total_calculate.win_count}승</span>
            <span id="total_losecount">${data.total_calculate.lose_count}패</span>
            <div id="kda">
                <div class="chart">
                    <span>승률</span>
                    <div class="text">
                        <strong id="total_winrate">${data.total_calculate.win_rate}%</strong>
                    </div>
                </div>
                <div class="info">
                    <div class="k-d-a">
                        <span id="total_kill">${data.total_calculate.total_kill}</span>
                        <span> / </span>
                        <span id="total_death">${data.total_calculate.total_death}</span>
                        <span> / </span>
                        <span id="total_assist">${data.total_calculate.total_assist}</span>
                    </div>
                    <div id="total_kda">${data.total_calculate.total_kda}:1</div>
                    <div id="total_killpart">킬관여 ${data.total_calculate.total_kill_part}%</div>
                </div>
            </div>
        </div>
        <div class="champions"></div>
        <div class="positions"></div>
    `;

    totalmatch.insertAdjacentHTML('beforeend', totalHTML);


    matches.forEach(match => {
        let itemsHTML = '';
        let runesHTML = '';
        let bluechampHTML = '';
        let redchampHTML = '';
        let detailHTML = '';
        let resultmatch = {};

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
            else {
                itemsHTML += `<li></li>`;
            }
            });

            if (match.search_player_main_rune) {
                runesHTML += `
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
                `;
            }
            else {
                runesHTML += `
                    <div class="rune">
                        <div class="augment augment--empty"></div>
                    </div>
                    <div class="rune">
                        <div class="augment augment--empty"></div>
                    </div>
                `;
            }

        for (let i = 1; i <= 10; i++) {
            if (Array.isArray(match[i])) {
                // 동적으로 생긴(html) 부분 json 형태로 만들기 위한 변수
                resultmatch[`${i}`] = match[i];
                match[i].forEach(item => {
                    if (i <= 5) {
                        bluechampHTML += `
                        <li class="team" style="list-style-type: none;">
                            <div class="team_icon" style="position: relative">
                                <img src="/static/img/champion_square/${item.championname}.png" width="16" height="16">
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
                                    <img src="/static/img/champion_square/${item.championname}.png" width="16" height="16">
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
        resultJson = JSON.stringify(resultmatch)
        matchHTML += `
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
                                        <img src="/static/img/champion_square/${match.search_player_champ}.png" width="48" height="48">
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
                                    ${runesHTML}
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
                <button class="detail" data-match-info='${resultJson}' match-result="${match.win_or_not_eng}" status="open">
                    ${detailHTML}
                </button>
            </div>
          </div>
        </li>
        `;
    });

    match_20_info.insertAdjacentHTML('beforeend', matchHTML);
}




const buttons = document.querySelectorAll('.game-type button');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            // 현재 선택된 버튼의 값
            count = 20;
            const original_btn = document.querySelector('.selected');
            const li = button.parentElement;
            if (li.classList.contains("notselected")) {
                original_btn.classList.remove('selected');
                original_btn.classList.add('notselected');
                li.classList.add("selected");
                li.classList.remove("notselected");
            }
            const buttonValue = button.value;
            let buttonIntValue;
            if (buttonValue == "TOTAL") {
                buttonIntValue = 9999;
            }
            else if (buttonValue =="SOLORANKED") {
                buttonIntValue = 420;
            }
            else if (buttonValue =="FLEXRANKED") {
                buttonIntValue = 440;
            }
            else if (buttonValue =="NORMAL") {
                buttonIntValue = 430;
            }
            else {
                buttonIntValue = 450;
            }
            changematch(buttonIntValue);
            match_20_info.innerHTML = '';
            totalmatch.innerHTML = '';

        });
    });