function display_detailmatch(data, result, gameItem) {
    
    let matchdetailHTML = '';
    let blueteamhtml = '';
    let redteamhtml = '';

    for (let player = 0; player < 5; player++) {
        let itemKey = [data[player][0].item0, data[player][0].item1, data[player][0].item2, data[player][0].item3, data[player][0].item4,
        data[player][0].item5, data[player][0].item6];
        let item = 0;
        let itemhtml = '';
        for (let num = 0; num < 7; num++) {
            item = itemKey[num];
            if (item != 0) {
                itemhtml += `
                    <div class="item">
                        <div class style="position: relative;">
                            <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/item/${item}.png" width="22">
                        </div>
                    </div>
                `;
            }
            else {
                itemhtml += `
                    <div class="item">
                        <div class="no-item"></div>
                    </div>
                `;
            }
            
        }
        blueteamhtml += `
            <tr class="overview-player">
                <td class="champion">
                    <a rel="noreferrer">
                        <div class style="position: relative;">
                            <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/champion/${data[player][0].championname}.png" width="32">
                            <div class="level">${data[player][0].champlevel}</div>
                        </div>
                    </a>
                </td>
                <td class="spells">
                    <div class style="position: relative;">
                        <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/spell/${data[player][0].summonerspell1}.png">
                    </div>
                    <div class style="position: relative;">
                        <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/spell/${data[player][0].summonerspell2}.png">
                    </div>
                </td>
                <td class="runes">
                    <div class style="position: relative;">
                        <img src="https://ddragon.canisback.com/img/${data[player][0].main_rune}" width="22" height="22">
                    </div>
                    <div class style="position: relative;">
                        <img src="https://ddragon.canisback.com/img/perk-images/Styles/${data[player][0].sub_rune}.png" width="22" height="22">
                    </div>
                </td>
                <td class="name">
                    <a href="/summoners/kr/${data[player][0].summonername}">${data[player][0].summonername}</a>
                    <div class="tier"></div>
                </td>
                <td class="killdeathassist">
                    <div class="k-d-a">
                        ${data[player][0].kills}/${data[player][0].deaths}/${data[player][0].assists}
                        <div class style="position: relative;">
                            (${data[player][0].killparticipation}%)
                        </div>
                    </div>
                    <div class="kda">
                        ${data[player][0].kda}:1
                    </div>
                </td>
                <td class="damage">
                    <div>
                        <div class style="position: relative;">
                            <div class="dealt">${data[player][0].totalDamageDealtToChampions}</div>
                            <div class="progress"></div>
                        </div>
                        <div class style="position: relative;">
                            <div class="taken">${data[player][0].totalDamageTaken}</div>
                            <div class="taken_progress"></div>
                        </div>
                    </div>
                </td>
                <td class="ward">
                    <div class style="position: relative;">
                        <div>${data[player][0].visionWardsBoughtInGame}</div>
                        <div>${data[player][0].wardsPlaced} / ${data[player][0].wardsKilled}</div>
                    </div>
                </td>
                <td class="cs">
                    <div>${data[player][0].totalminions_kill}</div>
                    <div>분당 ${data[player][0].minperminions}</div>
                </td>
                <td class="items">
                    ${itemhtml}
                </td>
            </tr>
        `;
    }

    for (let player = 5; player < 10; player++) {
        if (data[player] && data[player][0]) {
            let itemKey = [data[player][0].item0, data[player][0].item1, data[player][0].item2, data[player][0].item3, data[player][0].item4,
            data[player][0].item5, data[player][0].item6];
            let item = 0;
            let reditemhtml = '';
            for (let num = 0; num < 7; num++) {
                item = itemKey[num];
                if (item != 0) {
                    reditemhtml += `
                        <div class="item">
                            <div class style="position: relative;">
                                <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/item/${item}.png" width="22">
                            </div>
                        </div>
                    `;
                }
                else {
                    reditemhtml += `
                        <div class="item">
                            <div class="no-item"></div>
                        </div>
                    `;
                }
                
            }
            redteamhtml += `
                <tr class="overview-player">
                    <td class="champion">
                        <a>
                            <div class style="position: relative;">
                                <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/champion/${data[player][0].championname}.png" width="32">
                                <div class="level">${data[player][0].champlevel}</div>
                            </div>
                        </a>
                        
                    </td>
                    <td class="spells">
                        <div class style="position: relative;">
                            <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/spell/${data[player][0].summonerspell1}.png">
                        </div>
                        <div class style="position: relative;">
                            <img src="https://ddragon.leagueoflegends.com/cdn/13.20.1/img/spell/${data[player][0].summonerspell2}.png">
                        </div>
                    </td>
                    <td class="runes">
                        <div class style="position: relative;">
                            <img src="https://ddragon.canisback.com/img/${data[player][0].main_rune}" width="22" height="22">
                        </div>
                        <div class style="position: relative;">
                            <img src="https://ddragon.canisback.com/img/perk-images/Styles/${data[player][0].sub_rune}.png" width="22" height="22">
                        </div>
                    </td>
                    <td class="name">
                        <a href="/summoners/kr/${data[player][0].summonername}">${data[player][0].summonername}</a>
                        <div class="tier"></div>
                    </td>
                    <td class="killdeathassist">
                        <div class="k-d-a">
                            ${data[player][0].kills}/${data[player][0].deaths}/${data[player][0].assists}
                            <div class style="position: relative;">
                                (${data[player][0].killparticipation}%)
                            </div>
                        </div>
                        <div class="kda">
                            ${data[player][0].kda}:1
                        </div>
                    </td>
                    <td class="damage">
                        <div>
                            <div class style="position: relative;">
                                <div class="dealt">${data[player][0].totalDamageDealtToChampions}</div>
                                <div class="progress"></div>
                            </div>
                            <div class style="position: relative;">
                                <div class="taken">${data[player][0].totalDamageTaken}</div>
                                <div class="taken_progress"></div>
                            </div>
                        </div>
                    </td>
                    <td class="ward">
                        <div class style="position: relative;">
                            <div>${data[player][0].visionWardsBoughtInGame}</div>
                            <div>${data[player][0].wardsPlaced} / ${data[player][0].wardsKilled}</div>
                        </div>
                    </td>
                    <td class="cs">
                        <div>${data[player][0].totalminions_kill}</div>
                        <div>분당 ${data[player][0].minperminions}</div>
                    </td>
                    <td class="items">
                        ${reditemhtml}
                    </td>
                </tr>
                `;
        } else {
            continue;
        }
        
        }


    matchdetailHTML += `
        <div result="${result}" class="match_detail">
            <ul>
                <li class="total">
                    <button>종합</button>
                </li>
            </ul>
            <div class="totalteam">
                <table class="teamblue">
                    <colgroup>
                        <col width="44">
                        <col width="18">
                        <col width="18">
                        <col>
                        <col width="98">
                        <col width="120">
                        <col width="48">
                        <col width="56">
                        <col width="175">
                    </colgroup>
                    <thead>
                        <tr>
                            <th colspan="4"><span>블루팀</span></th>
                            <th>KDA</th>
                            <th>피해량</th>
                            <th>와드</th>
                            <th>CS</th>
                            <th>아이템</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${blueteamhtml}
                    </tbody>
                </table>
                <div class="summary">
                    <div class="team"></div>
                    <div class="summary-graph"></div>
                    <div class="team"></div>
                </div>
                <table class="teamred">
                    <colgroup>
                        <col width="44">
                        <col width="18">
                        <col width="18">
                        <col>
                        <col width="98">
                        <col width="120">
                        <col width="48">
                        <col width="56">
                        <col width="175">
                    </colgroup>
                    <thead>
                        <tr>
                            <th colspan="4"><span class="result">레드팀</span></th>
                            <th>KDA</th>
                            <th>피해량</th>
                            <th>와드</th>
                            <th>CS</th>
                            <th>아이템</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${redteamhtml}
                    </tbody>
                </table>
            </div>
        </div>
    `;

    gameItem.insertAdjacentHTML('beforeend', matchdetailHTML);
}

function delete_detailmatch(gameItem) {
    let matchDetail = gameItem.querySelector(".match_detail");
    matchDetail.remove();
}


const commonParent = document.querySelector('.match_20'); // 공통 상위 요소 선택

commonParent.addEventListener('click', function(event) {
    if (event.target.classList.contains('detail')) {
        // "detail" 버튼이 클릭된 경우 처리할 코드
        const button = event.target;
        let gameItem = button.closest(".game-item");
        let buttonstatus = button.getAttribute("status");

        if (buttonstatus === "open") {
            const match = [];
            const matchInfo = JSON.parse(button.getAttribute("data-match-info"));
            const matchResult = button.getAttribute("match-result");
            console.log("data-match-info:", matchInfo);
            console.log("match-result:", matchResult);
            for (let i = 1; i <= 10; i++) {
                match.push(matchInfo[i]);
            }
            button.setAttribute("status", "close");
            button.querySelector("img").style.transform = `rotate(${180}deg)`;
            display_detailmatch(match, matchResult, gameItem);
        } else {
            button.setAttribute("status", "open");
            button.querySelector("img").style.transform = `rotate(${0}deg)`;
            delete_detailmatch(gameItem);
        }
    }
});
