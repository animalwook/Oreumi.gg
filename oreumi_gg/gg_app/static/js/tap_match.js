const totalmatch = document.querySelector(".match_statics");
const match_20_info = document.querySelector(".match_20");

function changematch(queue, callback) {
    fetch(`/api/summoners_info/${country}/${summonerName}/${0}/${queue}`)
        .then(response => {
            if (!response.ok) {
                if (response.status === 503) {
                    throw new Error('서비스를 이용할 수 없습니다. 잠시 후 다시 시도해 주세요.');
                } else if (response.status === 500) {
                    throw new Error('서버 오류가 발생했습니다. 관리자에게 문의하세요.');
                } else if (response.status === 429) {
                    throw new Error('API 사용량 제한 초과. 나중에 다시 시도하세요.');
                } else {
                    throw new Error('알 수 없는 오류가 발생했습니다.');
                }
            }
            return response.json();
        })
        .then(data => {
            // 데이터 사용
            changematch_display(data);
            callback();
        })
        .catch(error => {
            console.error("API 호출 중 오류 발생:", error);
            // 오류 처리 로직을 추가하거나 사용자에게 오류 메시지를 표시하는 등의 작업을 수행합니다.
        });
}

function changematch_display(data) {
    
    let totalHTML = '';
    let matchHTML = '';
    totalmatch.innerHTML = '';
    const matches = data.matches;
    if (data.total_calculate.total_match_count != 0) {
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
                            <img src="/static/img/item/${ item }.webp" width="22" height="22">
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
                            <img src="/static/img/${match.search_player_main_rune}.webp" width="22" height="22">
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
                            <li class="team_outer" style="list-style-type: none;">
                                <div class="team_icon" style="position: relative">
                                    <img src="/static/img/champion_square_test/${item.championname}.webp" width="16" height="16">
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
                                <li class="team_outer" style="list-style-type: none;">
                                    <div class="team_icon" style="position: relative">
                                        <img src="/static/img/champion_square_test/${item.championname}.webp" width="16" height="16">
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
                                            <img src="/static/img/champion_square_test/${match.search_player_champ}.webp" width="48" height="48">
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
        
        if (data.total_calculate.total_match_count % 20 == 0) {
            fetchButton.style.display="block";
        }
    }
    else {
        totalHTML += `
            <div class="no-data">기록된 전적이 없습니다.</div>
        `
        totalmatch.insertAdjacentHTML('beforeend', totalHTML);
        match_20_info.insertAdjacentHTML('beforeend', matchHTML);
    }
}

const renewalbutton = document.querySelector('.renewal-button');

renewalbutton.addEventListener('click', () => {
    count = 20;
    changematch(9999, function() {

    });
    match_20_info.innerHTML = '';
    totalmatch.innerHTML = '<img src="/static/img/oreumi_gg/loading.gif" width="22" height="22" style="margin-left: 320px;">';
    fetchButton.style.display="none";
});


const buttons = document.querySelectorAll('.game-type button');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            // 현재 선택된 버튼의 값
            count = 20;
            const original_btn = document.querySelector('.selected');
            const li = button.parentElement;
            buttons.forEach(otherButton => {
                otherButton.disabled = true;
            });
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
            changematch(buttonIntValue, function() {
                buttons.forEach(otherButton => {
                    otherButton.disabled = false;
                });
            });
            match_20_info.innerHTML = '';
            totalmatch.innerHTML = '<img src="/static/img/oreumi_gg/loading.gif" width="22" height="22" style="margin-left: 320px;">';
            fetchButton.style.display="none";
        });
    });