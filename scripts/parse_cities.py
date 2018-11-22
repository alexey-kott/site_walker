from bs4 import BeautifulSoup


table = '''
    <table style="width: 659px;" class="table">
        <tbody>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Белгородская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1511620</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Белгород</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">337030</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">31</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Брянская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1378941</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Брянск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">431526</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">32</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Владимирская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1523990</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Владимир</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">315954</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">33</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Воронежская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2378803</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Воронеж</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">848752</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">36, 136</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Ивановская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1148329</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Иваново</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">431721</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">37</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Калужская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1041641</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Калуга</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">350633</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">40</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Костромская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">736641</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Кострома</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">278750</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">44</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Курская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1235091</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Курск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">412442</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">46</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Липецкая область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1213499</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Липецк</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">506114</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">48</span></td>
        </tr>
        <tr style="height: 48px;">
            <td style="height: 48px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 48px; width: 114px;"><span style="font-size: 8pt;">Москва</span></td>
            <td style="height: 48px; width: 59px;"><span style="font-size: 8pt;">10382754</span></td>
            <td style="height: 48px; width: 133px;"><span style="font-size: 8pt;">Москва</span></td>
            <td style="height: 48px; width: 93px;"><span style="font-size: 8pt;">10126424</span></td>
            <td style="height: 48px; width: 98px;"><span style="font-size: 8pt;">77, 97, 99, 177, 199, 197, 777</span>
            </td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Московская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">6618538</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Москва</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">&nbsp;</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">50, 90, 150, 190, 750</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Орловская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">860262</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Орел</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">333310</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">57</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Рязанская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1227910</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Рязань</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">521560</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">62</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Смоленская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1049574</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Смоленск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">325137</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">67</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Тамбовская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1178443</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Тамбов</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">293658</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">68</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Тверская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1471459</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Тверь</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">408903</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">69, 169</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Тульская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1675758</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Тула</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">481216</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">71</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Центральный&nbsp; ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Ярославская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1367398</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Ярославль</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">613088</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">76</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Северо-Западный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Архангельская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1336539</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Архангельск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">362327</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">29</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Северо-Западный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Вологодская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1269568</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Вологда</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">293046</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">35</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Северо-Западный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Калининградская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">955281</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Калининград</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">430003</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">39, 91</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Северо-Западный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Карелия</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">716281</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Петрозаводск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">266589</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">10</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Северо-Западный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Коми</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1018674</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Сыктывкар</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">230011</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">11</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Северо-Западный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Ленинградская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1669205</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Санкт-Петербург</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">&nbsp;</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">47</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Северо-Западный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Мурманская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">892534</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Мурманск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">336137</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">51</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Северо-Западный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Ненецкий автономный округ</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">41546</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Салехард</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">48467</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">83</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Северо-Западный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Новгородская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">694355</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Великий Новгород</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">216856</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">53</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Северо-Западный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Псковская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">760810</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Псков</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">202780</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">60</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Северо-Западный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Санкт-Петербург</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">4661219</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Санкт-Петербург</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">4661219</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">78, 98, 178</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Башкортостан</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">4104336</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Уфа</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">1049479</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">02, 102</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Кировская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1503529</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Киров</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">457578</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">43</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Марий Эл</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">727979</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Йошкар-Ола</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">281165</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">12</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Мордовия</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">888766</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Саранск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">304866</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">13, 113</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Нижегородская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">3524028</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Нижний Новгород</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">1311252</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">52, 152</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Оренбургская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2179551</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Оренбург</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">549361</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">56</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Пензенская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1452941</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Пенза</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">518437</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">58</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Пермский край</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2633774</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Пермь</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">1001653</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">59, 81, 159</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Самарская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">3239737</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Самара</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">1157880</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">63, 163</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Саратовская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2668310</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Саратов</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">873055</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">64, 164</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Татарстан</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">3779265</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Казань</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">1105306</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">16, 116</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Удмуртская Республика</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1570316</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Ижевск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">632140</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">18</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Ульяновская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1382811</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Ульяновск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">657498</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">73, 173</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Приволжский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Чувашская Республика</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1313754</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Чебоксары</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">440621</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">21, 121</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Уральский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Курганская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1019532</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Курган</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">345515</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">45</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Уральский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Свердловская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">4486214</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Екатеринбург</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">1293537</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">66, 96, 196</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Уральский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Тюменская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">3264841</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Тюмень</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">510719</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">72</span></td>
        </tr>
        <tr style="height: 48px;">
            <td style="height: 48px; width: 122px;"><span style="font-size: 8pt;">Уральский ФО</span></td>
            <td style="height: 48px; width: 114px;"><span style="font-size: 8pt;">Ханты-Мансийский автономный округ — Югра</span>
            </td>
            <td style="height: 48px; width: 59px;"><span style="font-size: 8pt;">1432817</span></td>
            <td style="height: 48px; width: 133px;"><span style="font-size: 8pt;">Ханты-мансийск</span></td>
            <td style="height: 48px; width: 93px;"><span style="font-size: 8pt;">53953</span></td>
            <td style="height: 48px; width: 98px;"><span style="font-size: 8pt;">86, 186</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Уральский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Челябинская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">3603339</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Челябиннск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">1104648</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">74, 174</span></td>
        </tr>
        <tr style="height: 48px;">
            <td style="height: 48px; width: 122px;"><span style="font-size: 8pt;">Уральский ФО</span></td>
            <td style="height: 48px; width: 114px;"><span style="font-size: 8pt;">Ямало-Ненецкий автономный округ</span>
            </td>
            <td style="height: 48px; width: 59px;"><span style="font-size: 8pt;">507006</span></td>
            <td style="height: 48px; width: 133px;"><span style="font-size: 8pt;">Салехард</span></td>
            <td style="height: 48px; width: 93px;"><span style="font-size: 8pt;">37035</span></td>
            <td style="height: 48px; width: 98px;"><span style="font-size: 8pt;">89</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Алтай</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">202947</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Горно-Алтайск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">53538</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">4</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Алтайский край</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2607426</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Барнаул</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">600749</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">22</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Бурятия</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">981238</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Улан-Удэ</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">386880</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">3</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Забайкальский край</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1082633</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Чита</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">317183</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">75, 80</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Иркутская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2581705</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Иркутск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">593604</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">38, 85, 138</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Кемеровская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2899142</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Кемерово</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">484754</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">42, 142</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Красноярский край</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2966042</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Красноярск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">909341</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">24, 84, 88, 124</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Новосибирская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2692251</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Новосибирск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">1425508</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">54, 154</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Омская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2079220</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Омск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">1134016</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">55</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Томская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1046039</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Томск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">487838</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">70</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Тыва</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">305510</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Кызыл</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">104105</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">17</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Сибирский ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Хакасия</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">546072</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Абакан</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">165197</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">19</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Дальневосточный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Амурская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">902844</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Благовещенск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">32989</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">28</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Дальневосточный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Еврейская автономная область</span>
            </td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">190915</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Биробиджан</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">77250</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">79</span></td>
        </tr>
        <tr style="height: 48px;">
            <td style="height: 48px; width: 122px;"><span style="font-size: 8pt;">Дальневосточный ФО</span></td>
            <td style="height: 48px; width: 114px;"><span style="font-size: 8pt;">Камчатская область</span></td>
            <td style="height: 48px; width: 59px;"><span style="font-size: 8pt;">358801</span></td>
            <td style="height: 48px; width: 133px;"><span style="font-size: 8pt;">Петропавловск-Камчатский</span></td>
            <td style="height: 48px; width: 93px;"><span style="font-size: 8pt;">198028</span></td>
            <td style="height: 48px; width: 98px;"><span style="font-size: 8pt;">#Н/Д</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Дальневосточный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Магаданская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">182726</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Магадан</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">99399</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">49</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Дальневосточный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Приморский край</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2071210</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Владивосток</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">594701</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">25, 125</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Дальневосточный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Саха (Якутия)</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">949280</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Якутск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">210642</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">14</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Дальневосточный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Сахалинская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">546695</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Южно-Сахалинск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">175085</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">65</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Дальневосточный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Хабаровский край</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1436570</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Хабаровск</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">583072</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">27, 127</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Дальневосточный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Чукотский автономный округ</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">53824</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Анадырь</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">11038</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">87</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Южный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Адыгея</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">447109</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Майкоп</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">175753</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">1</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Южный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Астраханская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">1005276</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Астрахань</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">504501</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">30</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Южный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Волгоградская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">2699223</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Волгоград</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">1011417</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">34, 134</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Южный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Республика Калмыкия</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">292410</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Элиста</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">108511</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">8</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Южный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Краснодарский край</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">5125221</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Краснодар</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">646175</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">23, 93, 123</span></td>
        </tr>
        <tr style="height: 24px;">
            <td style="height: 24px; width: 122px;"><span style="font-size: 8pt;">Южный ФО</span></td>
            <td style="height: 24px; width: 114px;"><span style="font-size: 8pt;">Ростовская область</span></td>
            <td style="height: 24px; width: 59px;"><span style="font-size: 8pt;">4404013</span></td>
            <td style="height: 24px; width: 133px;"><span style="font-size: 8pt;">Ростов</span></td>
            <td style="height: 24px; width: 93px;"><span style="font-size: 8pt;">34141</span></td>
            <td style="height: 24px; width: 98px;"><span style="font-size: 8pt;">61, 161</span></td>
        </tr>
        <tr style="height: 48px;">
            <td style="height: 48px; width: 122px;"><span style="font-size: 8pt;">Северо-Кавказский ФО</span></td>
            <td style="height: 48px; width: 114px;"><span style="font-size: 8pt;">Республика Дагестан</span></td>
            <td style="height: 48px; width: 59px;"><span style="font-size: 8pt;">2576531</span></td>
            <td style="height: 48px; width: 133px;"><span style="font-size: 8pt;">Махачкала</span></td>
            <td style="height: 48px; width: 93px;"><span style="font-size: 8pt;">462412</span></td>
            <td style="height: 48px; width: 98px;"><span style="font-size: 8pt;">5</span></td>
        </tr>
        <tr style="height: 48px;">
            <td style="height: 48px; width: 122px;"><span style="font-size: 8pt;">Северо-Кавказский ФО</span></td>
            <td style="height: 48px; width: 114px;"><span style="font-size: 8pt;">Республика Ингушетия</span></td>
            <td style="height: 48px; width: 59px;"><span style="font-size: 8pt;">467294</span></td>
            <td style="height: 48px; width: 133px;"><span style="font-size: 8pt;">Магас</span></td>
            <td style="height: 48px; width: 93px;"><span style="font-size: 8pt;">275</span></td>
            <td style="height: 48px; width: 98px;"><span style="font-size: 8pt;">6</span></td>
        </tr>
        <tr style="height: 48px;">
            <td style="height: 48px; width: 122px;"><span style="font-size: 8pt;">Северо-Кавказский ФО</span></td>
            <td style="height: 48px; width: 114px;"><span
                    style="font-size: 8pt;">Кабардино — Балкарская Республика</span></td>
            <td style="height: 48px; width: 59px;"><span style="font-size: 8pt;">901494</span></td>
            <td style="height: 48px; width: 133px;"><span style="font-size: 8pt;">Нальчик</span></td>
            <td style="height: 48px; width: 93px;"><span style="font-size: 8pt;">274974</span></td>
            <td style="height: 48px; width: 98px;"><span style="font-size: 8pt;">7</span></td>
        </tr>
        <tr style="height: 48px;">
            <td style="height: 48px; width: 122px;"><span style="font-size: 8pt;">Северо-Кавказский ФО</span></td>
            <td style="height: 48px; width: 114px;"><span
                    style="font-size: 8pt;">Карачаево — Черкесская Республика</span></td>
            <td style="height: 48px; width: 59px;"><span style="font-size: 8pt;">439470</span></td>
            <td style="height: 48px; width: 133px;"><span style="font-size: 8pt;">Черкесск</span></td>
            <td style="height: 48px; width: 93px;"><span style="font-size: 8pt;">116244</span></td>
            <td style="height: 48px; width: 98px;"><span style="font-size: 8pt;">9</span></td>
        </tr>
        <tr style="height: 48px;">
            <td style="height: 48px; width: 122px;"><span style="font-size: 8pt;">Северо-Кавказский ФО</span></td>
            <td style="height: 48px; width: 114px;"><span
                    style="font-size: 8pt;">Республика Северная Осетия-Алания</span></td>
            <td style="height: 48px; width: 59px;"><span style="font-size: 8pt;">710275</span></td>
            <td style="height: 48px; width: 133px;"><span style="font-size: 8pt;">Владивкавказ</span></td>
            <td style="height: 48px; width: 93px;"><span style="font-size: 8pt;">332650</span></td>
            <td style="height: 48px; width: 98px;"><span style="font-size: 8pt;">15</span></td>
        </tr>
        <tr style="height: 48px;">
            <td style="height: 48px; width: 122px;"><span style="font-size: 8pt;">Северо-Кавказский ФО</span></td>
            <td style="height: 48px; width: 114px;"><span style="font-size: 8pt;">Ставропольский край</span></td>
            <td style="height: 48px; width: 59px;"><span style="font-size: 8pt;">2735139</span></td>
            <td style="height: 48px; width: 133px;"><span style="font-size: 8pt;">Ставрополь</span></td>
            <td style="height: 48px; width: 93px;"><span style="font-size: 8pt;">355066</span></td>
            <td style="height: 48px; width: 98px;"><span style="font-size: 8pt;">26, 126</span></td>
        </tr>
        <tr style="height: 48px;">
            <td style="height: 48px; width: 122px;"><span style="font-size: 8pt;">Северо-Кавказский ФО</span></td>
            <td style="height: 48px; width: 114px;"><span style="font-size: 8pt;">Чеченская Республика</span></td>
            <td style="height: 48px; width: 59px;"><span style="font-size: 8pt;">1103686</span></td>
            <td style="height: 48px; width: 133px;"><span style="font-size: 8pt;">Грозный</span></td>
            <td style="height: 48px; width: 93px;"><span style="font-size: 8pt;">210720</span></td>
            <td style="height: 48px; width: 98px;"><span style="font-size: 8pt;">95</span></td>
        </tr>
        </tbody>
    </table>'''

from walker_panel.models import City

def run():
    soup = BeautifulSoup(table, 'lxml')
    t = soup.find('table')

    cities = []
    for tr in t.find_all('tr'):
        cities.append(tr.find_all('td')[3].text)

    city = City(name='')
    city.save()

    for item in sorted(cities):
        try:
            city = City(name=item)
            city.save()
        except:
            print(item)
