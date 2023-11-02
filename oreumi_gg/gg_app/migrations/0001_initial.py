# Generated by Django 4.2.6 on 2023-11-02 14:53

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('author', models.CharField(default='admin', max_length=200)),
                ('view', models.IntegerField(default=0)),
                ('category', models.CharField(default='자유게시판', max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('up', models.PositiveIntegerField(default=0)),
                ('down', models.PositiveIntegerField(default=0)),
                ('comment_count', models.PositiveIntegerField(default=0)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('room_number', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('latest_message_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='User', max_length=255)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatchIDModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchId', models.CharField(max_length=200)),
                ('matchSummonerList', models.CharField(default='', max_length=255)),
                ('game_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MatchInfoDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playernumber', models.PositiveIntegerField()),
                ('kills', models.PositiveIntegerField(blank=True, null=True)),
                ('assists', models.PositiveIntegerField(blank=True, null=True)),
                ('deaths', models.PositiveIntegerField(blank=True, null=True)),
                ('summonername', models.CharField(blank=True, max_length=40, null=True)),
                ('championname', models.CharField(blank=True, max_length=20, null=True)),
                ('teamposition', models.CharField(blank=True, max_length=10, null=True)),
                ('teamid', models.PositiveIntegerField(blank=True, null=True)),
                ('item0', models.PositiveIntegerField(blank=True, null=True)),
                ('item1', models.PositiveIntegerField(blank=True, null=True)),
                ('item2', models.PositiveIntegerField(blank=True, null=True)),
                ('item3', models.PositiveIntegerField(blank=True, null=True)),
                ('item4', models.PositiveIntegerField(blank=True, null=True)),
                ('item5', models.PositiveIntegerField(blank=True, null=True)),
                ('item6', models.PositiveIntegerField(blank=True, null=True)),
                ('totalminions_kill', models.PositiveIntegerField(blank=True, null=True)),
                ('wardsKilled', models.PositiveIntegerField(blank=True, null=True)),
                ('wardsPlaced', models.PositiveIntegerField(blank=True, null=True)),
                ('visionWardsBoughtInGame', models.PositiveIntegerField(blank=True, null=True)),
                ('summonerspell1', models.CharField(blank=True, max_length=30, null=True)),
                ('summonerspell2', models.CharField(blank=True, max_length=30, null=True)),
                ('kda', models.CharField(blank=True, max_length=30, null=True)),
                ('killparticipation', models.PositiveIntegerField(blank=True, null=True)),
                ('totalDamageDealtToChampions', models.PositiveIntegerField(blank=True, null=True)),
                ('totalDamageTaken', models.PositiveIntegerField(blank=True, null=True)),
                ('champlevel', models.PositiveIntegerField(blank=True, null=True)),
                ('main_rune', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_rune', models.CharField(blank=True, max_length=200, null=True)),
                ('minperminions', models.FloatField(blank=True, null=True)),
                ('placement', models.FloatField(blank=True, null=True)),
                ('goldearned', models.PositiveIntegerField(blank=True, null=True)),
                ('win', models.BooleanField(blank=True, null=True)),
                ('dragon_kills', models.PositiveIntegerField(blank=True, null=True)),
                ('turret_kills', models.PositiveIntegerField(blank=True, null=True)),
                ('baron_kills', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatchInfoForSearchPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summonername', models.CharField(max_length=20)),
                ('game_playtime', models.CharField(blank=True, max_length=20, null=True)),
                ('game_type', models.CharField(blank=True, max_length=20, null=True)),
                ('win_or_not', models.CharField(blank=True, max_length=20, null=True)),
                ('win_or_not_eng', models.CharField(blank=True, max_length=20, null=True)),
                ('search_player_kill', models.PositiveIntegerField(blank=True, null=True)),
                ('search_player_death', models.PositiveIntegerField(blank=True, null=True)),
                ('search_player_assist', models.PositiveIntegerField(blank=True, null=True)),
                ('game_time', models.CharField(blank=True, max_length=20, null=True)),
                ('search_player_champ', models.CharField(blank=True, max_length=20, null=True)),
                ('search_player_kda', models.CharField(blank=True, max_length=20, null=True)),
                ('search_player_killpart', models.PositiveIntegerField(blank=True, null=True)),
                ('search_player_main_rune', models.CharField(blank=True, max_length=100, null=True)),
                ('search_player_sub_rune', models.CharField(blank=True, max_length=20, null=True)),
                ('search_player_summonerspell1', models.CharField(blank=True, max_length=20, null=True)),
                ('search_player_summonerspell2', models.CharField(blank=True, max_length=20, null=True)),
                ('search_player_item', models.TextField(blank=True, null=True)),
                ('search_player_champlevel', models.PositiveIntegerField(blank=True, null=True)),
                ('search_player_totalminions_kill', models.PositiveIntegerField(blank=True, null=True)),
                ('search_player_visionWardsBoughtInGame', models.PositiveIntegerField(blank=True, null=True)),
                ('search_player_minperminions', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='SoloRankList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.PositiveIntegerField(blank=True, null=True)),
                ('summoners', models.CharField(blank=True, max_length=40, null=True)),
                ('tier', models.CharField(blank=True, max_length=80, null=True)),
                ('rank', models.CharField(blank=True, max_length=10, null=True)),
                ('LP', models.PositiveIntegerField(blank=True, null=True)),
                ('level', models.PositiveIntegerField(blank=True, null=True)),
                ('win', models.PositiveIntegerField(blank=True, null=True)),
                ('lose', models.PositiveIntegerField(blank=True, null=True)),
                ('winlate', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SummonerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puuid', models.CharField(max_length=200)),
                ('search_player_tear_by_season', models.CharField(max_length=200)),
                ('search_player_ranking', models.PositiveIntegerField()),
                ('search_player_name', models.CharField(max_length=40)),
                ('search_player_name_strip', models.CharField(max_length=40)),
                ('search_player_icon', models.CharField(max_length=200)),
                ('search_player_level', models.PositiveIntegerField()),
                ('search_player_updated_at', models.DateTimeField(auto_now=True)),
                ('search_player_is_read', models.BooleanField(default=False)),
                ('search_player_solo_tear', models.CharField(blank=True, max_length=80, null=True)),
                ('search_player_solo_rank', models.CharField(blank=True, max_length=10, null=True)),
                ('search_player_solo_points', models.PositiveIntegerField(blank=True, null=True)),
                ('search_player_solo_wins', models.PositiveIntegerField(blank=True, null=True)),
                ('search_player_solo_losses', models.PositiveIntegerField(blank=True, null=True)),
                ('search_player_flex_tear', models.CharField(blank=True, max_length=80, null=True)),
                ('search_player_flex_rank', models.CharField(blank=True, max_length=10, null=True)),
                ('search_player_flex_points', models.PositiveIntegerField(blank=True, null=True)),
                ('search_player_flex_wins', models.PositiveIntegerField(blank=True, null=True)),
                ('search_player_flex_losses', models.PositiveIntegerField(blank=True, null=True)),
                ('most1', models.CharField(default='', max_length=80)),
                ('most2', models.CharField(default='', max_length=80)),
                ('most3', models.CharField(default='', max_length=80)),
            ],
        ),
    ]
