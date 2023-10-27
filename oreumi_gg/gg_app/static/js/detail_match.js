function display_detailmatch(data, result, gameItem, gameminute, maxdealt, maxtaken) {
    /**
     * 
     * 매치 상세 정보를 보여주는 함수
     * 일반 매치와 아레나의 숫자가 다르기 때문에 if문으로 조건을 줌
     * 
     */
    if (data[8]) {
        let win_or_lose = data[0][0].win;
        let blueteam_win = "";
        let redteam_win = "";
        if (gameminute > 3) {
            if (win_or_lose == true) {
                blueteam_win = "(승리)"
                redteam_win = "(패배)"
            } else {
                blueteam_win = "(패배)"
                redteam_win = "(승리)"
            }
        }
        
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
                                <img src="/static/img/item/${item}.webp" width="22">
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
                                <img src="/static/img/champion_square_test/${data[player][0].championname}.webp" width="32">
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
                            <img src="/static/img/${data[player][0].main_rune}.webp" width="22" height="22">
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
                            <div class="deal_box" style="position: relative;">
                                <div class="dealt">${data[player][0].totalDamageDealtToChampions}</div>
                                <span class="dealt_tooltip dealt_tooltiptop">챔피언에게 가한 피해량:${data[player][0].totalDamageDealtToChampions}</span>
                                <div class="progress">
                                    <div class="fill" style="width: ${Math.round((data[player][0].totalDamageDealtToChampions / maxdealt) * 100)}%"></div>
                                </div>
                            </div>
                            <div class="taken_box" style="position: relative;">
                                <div class="taken">${data[player][0].totalDamageTaken}</div>
                                <span class="taken_tooltip taken_tooltiptop">받은 피해량:${data[player][0].totalDamageTaken}</span>
                                <div class="taken_progress">
                                    <div class="fill" style="width: ${Math.round((data[player][0].totalDamageTaken / maxtaken) * 100)}%"></div>
                                </div>
                            </div>
                        </div>
                    </td>
                    <td class="ward">
                        <div class="ward_info" style="position: relative;">
                            <div>${data[player][0].visionWardsBoughtInGame}</div>
                            <div>${data[player][0].wardsPlaced} / ${data[player][0].wardsKilled}</div>
                        </div>
                        <span class="ward_tooltip">
                                제어와드:${data[player][0].visionWardsBoughtInGame}
                                와드설치:${data[player][0].wardsPlaced}
                                와드제거:${data[player][0].wardsKilled}
                            </span>
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
                                <img src="/static/img/item/${item}.webp" width="22">
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
                                <img src="/static/img/champion_square_test/${data[player][0].championname}.webp" width="32">
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
                            <img src="/static/img/${data[player][0].main_rune}.webp" width="22" height="22">
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
                            <div class="deal_box" style="position: relative;">
                                <div class="dealt">${data[player][0].totalDamageDealtToChampions}</div>
                                <span class="dealt_tooltip dealt_tooltiptop">챔피언에게 가한 피해량:${data[player][0].totalDamageDealtToChampions}</span>
                                <div class="progress">
                                    <div class="fill" style="width: ${Math.round((data[player][0].totalDamageDealtToChampions / maxdealt) * 100)}%"></div>
                                </div>
                            </div>
                            <div class="taken_box" style="position: relative;">
                                <div class="taken">${data[player][0].totalDamageTaken}</div>
                                <span class="taken_tooltip taken_tooltiptop">받은 피해량:${data[player][0].totalDamageTaken}</span>
                                <div class="taken_progress">
                                    <div class="fill" style="width: ${Math.round((data[player][0].totalDamageTaken / maxtaken) * 100)}%"></div>
                                </div>
                            </div>
                        </div>
                    </td>
                    <td class="ward">
                        <div class="ward_info" style="position: relative;">
                            <div>${data[player][0].visionWardsBoughtInGame}</div>
                            <div>${data[player][0].wardsPlaced} / ${data[player][0].wardsKilled}</div>
                        </div>
                        <span class="ward_tooltip">
                                제어와드:${data[player][0].visionWardsBoughtInGame}
                                와드설치:${data[player][0].wardsPlaced}
                                와드제거:${data[player][0].wardsKilled}
                            </span>
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
                                <th colspan="4"><span class="result">블루팀 ${blueteam_win}</span></th>
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
                                <th colspan="4"><span class="result">레드팀 ${redteam_win}</span></th>
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
    else {
        let matchdetailHTML = '';
        let firstteamhtml = '';
        let secondteamhtml = '';
        let thirdteamhtml = '';
        let fourthteamhtml = '';
        for (let player = 0; player < 8; player++) {
            let itemKey = [data[player][0].item0, data[player][0].item1, data[player][0].item2, data[player][0].item3, data[player][0].item4,
            data[player][0].item5, data[player][0].item6];
            let item = 0;
            let itemhtml = '';
            let seconditemhtml = '';
            let thirditemhtml = '';
            let fourthitemhtml = '';
            if (data[player][0].placement == 1) { 
                for (let num = 0; num < 7; num++) {
                    item = itemKey[num];
                    if (item != 0) {
                        itemhtml += `
                            <div class="item">
                                <div class style="position: relative;">
                                    <img src="/static/img/item/${item}.webp" width="22">
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
                firstteamhtml += `
                    <tr class="overview-player">
                        <td class="champion">
                            <a>
                                <div class style="position: relative;">
                                    <img src="/static/img/champion_square_test/${data[player][0].championname}.webp" width="32">
                                    <div class="level">${data[player][0].champlevel}</div>
                                </div>
                            </a>
                        </td>
                        <td class="augments">
                            <div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
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
                                    <div class="progress">
                                        <div class="fill" style="width: ${Math.round((data[player][0].totalDamageDealtToChampions / maxdealt) * 100)}%"></div>
                                    </div>
                                </div>
                                <div class style="position: relative;">
                                    <div class="taken">${data[player][0].totalDamageTaken}</div>
                                    <div class="taken_progress">
                                        <div class="fill" style="width: ${Math.round((data[player][0].totalDamageTaken / maxtaken) * 100)}%"></div>
                                    </div>
                                </div>
                            </div>
                        </td>
                        <td class="gold">${data[player][0].goldearned}</td>
                        <td class="items">
                            ${itemhtml}
                        </td>
                    </tr>
                `;
            }
            else if (data[player][0].placement == 2) {
                for (let num = 0; num < 7; num++) {
                    item = itemKey[num];
                    if (item != 0) {
                        seconditemhtml += `
                            <div class="item">
                                <div class style="position: relative;">
                                    <img src="/static/img/item/${item}.webp" width="22">
                                </div>
                            </div>
                        `;
                    }
                    else {
                        seconditemhtml += `
                            <div class="item">
                                <div class="no-item"></div>
                            </div>
                        `;
                    }
                }
                secondteamhtml += `
                    <tr class="overview-player">
                        <td class="champion">
                            <a>
                                <div class style="position: relative;">
                                    <img src="/static/img/champion_square_test/${data[player][0].championname}.webp" width="32">
                                    <div class="level">${data[player][0].champlevel}</div>
                                </div>
                            </a>
                        </td>
                        <td class="augments">
                            <div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
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
                                    <div class="progress">
                                        <div class="fill" style="width: ${Math.round((data[player][0].totalDamageDealtToChampions / maxdealt) * 100)}%"></div>
                                    </div>
                                </div>
                                <div class style="position: relative;">
                                    <div class="taken">${data[player][0].totalDamageTaken}</div>
                                    <div class="taken_progress">
                                        <div class="fill" style="width: ${Math.round((data[player][0].totalDamageTaken / maxtaken) * 100)}%"></div>
                                    </div>
                                </div>
                            </div>
                        </td>
                        <td class="gold">${data[player][0].goldearned}</td>
                        <td class="items">
                            ${seconditemhtml}
                        </td>
                    </tr>
                `;
            }

            else if (data[player][0].placement == 3) {
                for (let num = 0; num < 7; num++) {
                    item = itemKey[num];
                    if (item != 0) {
                        thirditemhtml += `
                            <div class="item">
                                <div class style="position: relative;">
                                    <img src="/static/img/item/${item}.webp" width="22">
                                </div>
                            </div>
                        `;
                    }
                    else {
                        thirditemhtml += `
                            <div class="item">
                                <div class="no-item"></div>
                            </div>
                        `;
                    }
                }
                thirdteamhtml += `
                    <tr class="overview-player">
                        <td class="champion">
                            <a>
                                <div class style="position: relative;">
                                    <img src="/static/img/champion_square_test/${data[player][0].championname}.webp" width="32">
                                    <div class="level">${data[player][0].champlevel}</div>
                                </div>
                            </a>
                        </td>
                        <td class="augments">
                            <div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
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
                                    <div class="progress">
                                        <div class="fill" style="width: ${Math.round((data[player][0].totalDamageDealtToChampions / maxdealt) * 100)}%"></div>
                                    </div>
                                </div>
                                <div class style="position: relative;">
                                    <div class="taken">${data[player][0].totalDamageTaken}</div>
                                    <div class="taken_progress">
                                        <div class="fill" style="width: ${Math.round((data[player][0].totalDamageTaken / maxtaken) * 100)}%"></div>
                                    </div>
                                </div>
                            </div>
                        </td>
                        <td class="gold">${data[player][0].goldearned}</td>
                        <td class="items">
                            ${thirditemhtml}
                        </td>
                    </tr>
                `;
            }
            else {
                for (let num = 0; num < 7; num++) {
                    item = itemKey[num];
                    if (item != 0) {
                        fourthitemhtml += `
                            <div class="item">
                                <div class style="position: relative;">
                                    <img src="/static/img/item/${item}.webp" width="22">
                                </div>
                            </div>
                        `;
                    }
                    else {
                        fourthitemhtml += `
                            <div class="item">
                                <div class="no-item"></div>
                            </div>
                        `;
                    }
                }
                fourthteamhtml += `
                    <tr class="overview-player">
                        <td class="champion">
                            <a>
                                <div class style="position: relative;">
                                    <img src="/static/img/champion_square_test/${data[player][0].championname}.webp" width="32">
                                    <div class="level">${data[player][0].champlevel}</div>
                                </div>
                            </a>
                        </td>
                        <td class="augments">
                            <div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
                                <div class="augment augment--empty"></div>
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
                                    <div class="progress">
                                        <div class="fill" style="width: ${Math.round((data[player][0].totalDamageDealtToChampions / maxdealt) * 100)}%"></div>
                                    </div>
                                </div>
                                <div class style="position: relative;">
                                    <div class="taken">${data[player][0].totalDamageTaken}</div>
                                    <div class="taken_progress">
                                        <div class="fill" style="width: ${Math.round((data[player][0].totalDamageTaken / maxtaken) * 100)}%"></div>
                                    </div>
                                </div>
                            </div>
                        </td>
                        <td class="gold">${data[player][0].goldearned}</td>
                        <td class="items">
                            ${fourthitemhtml}
                        </td>
                    </tr>
                `;
            }
            
        }


        matchdetailHTML += `
            <div result="${result}" class="match_detail">
                <table class="overview-arena overview-arena--result-1">
                    <colgroup>
                        <col width="42">
                        <col width="32">
                        <col>
                        <col width="102">
                        <col width="116">
                        <col width="102">
                        <col width="174">
                    </colgroup>
                    <thead>
                        <tr>
                            <th class="placement" colspan="3">
                                <b>1st</b>
                            </th>
                            <th>평점</th>
                            <th>피해량</th>
                            <th>골드</th>
                            <th>아이템</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${firstteamhtml}
                    </tbody>
                </table>
                <table class="overview-arena overview-arena--result-2 overview-arena-other">
                    <colgroup>
                        <col width="42">
                        <col width="32">
                        <col>
                        <col width="102">
                        <col width="116">
                        <col width="102">
                        <col width="174">
                    </colgroup>
                    <thead>
                        <tr>
                            <th class="placement" colspan="3">
                                <b>2nd</b>
                            </th>
                            <th>평점</th>
                            <th>피해량</th>
                            <th>골드</th>
                            <th>아이템</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${secondteamhtml}
                    </tbody>
                </table>
                <table class="overview-arena overview-arena--result-3 overview-arena-other">
                    <colgroup>
                        <col width="42">
                        <col width="32">
                        <col>
                        <col width="102">
                        <col width="116">
                        <col width="102">
                        <col width="174">
                    </colgroup>
                    <thead>
                        <tr>
                            <th class="placement" colspan="3">
                                <b>3rd</b>
                            </th>
                            <th>평점</th>
                            <th>피해량</th>
                            <th>골드</th>
                            <th>아이템</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${thirdteamhtml}
                    </tbody>
                </table>
                <table class="overview-arena overview-arena--result-4 overview-arena-other">
                    <colgroup>
                        <col width="42">
                        <col width="32">
                        <col>
                        <col width="102">
                        <col width="116">
                        <col width="102">
                        <col width="174">
                    </colgroup>
                    <thead>
                        <tr>
                            <th class="placement" colspan="3">
                                <b>4th</b>
                            </th>
                            <th>평점</th>
                            <th>피해량</th>
                            <th>골드</th>
                            <th>아이템</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${fourthteamhtml}
                    </tbody>
                
                </table>
            </div>
        `;
        gameItem.insertAdjacentHTML('beforeend', matchdetailHTML);
    }
    
}

function delete_detailmatch(gameItem) {
    /** 
     * 클래스를 집어넣으면 해당 클래스에서 match_detail을 찾아 지움
     * 전적 상세 정보를 닫을 때 사용하는 함수
     */
    let matchDetail = gameItem.querySelector(".match_detail");
    matchDetail.remove();
}


const commonParent = document.querySelector('.match_20'); // 공통 상위 요소 선택



commonParent.addEventListener('click', function(event) {
    // 옆 버튼을 찾아 해당 버튼을 누르면 이벤트 일어나도록 함
    if (event.target.closest('.action')) {
        // "detail" 버튼이 클릭된 경우 처리할 코드
        const actiondiv = event.target.closest('.action');
        const button = actiondiv.querySelector('.detail');
        let gameItem = button.closest(".game-item");
        let buttonstatus = button.getAttribute("status");
        let gameDuration = gameItem.querySelector(".length");
        let gameminute = (gameDuration.textContent).split(" ")[0];
        gameminute = parseInt(gameminute)

        if (buttonstatus === "open") {
            const match = [];
            const dealt = [];
            const taken = [];
            const matchInfo = JSON.parse(button.getAttribute("data-match-info"));
            const matchResult = button.getAttribute("match-result");
            for (let i = 1; i <= 10; i++) {
                match.push(matchInfo[i]);
                if (matchInfo[i]) {
                    dealt.push(matchInfo[i][0].totalDamageDealtToChampions);
                    taken.push(matchInfo[i][0].totalDamageTaken);
                }
            }
            maxdealt = Math.max(...dealt);
            maxtaken = Math.max(...taken);
            button.setAttribute("status", "close");
            button.querySelector("img").style.transform = `rotate(${180}deg)`;
            display_detailmatch(match, matchResult, gameItem, gameminute, maxdealt, maxtaken);
        } else {
            button.setAttribute("status", "open");
            button.querySelector("img").style.transform = `rotate(${0}deg)`;
            delete_detailmatch(gameItem);
        }
    }
});
    


