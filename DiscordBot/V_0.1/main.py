import discord

class chatbot(discord.Client):
    # 프로그램 실행시 초기 구성
    async def on_ready(self):
        # 상태 메시지
        # 종류는: Gaming, Streaming, CustomActivity
        game = discord.Game("Coding")
        music = discord.CustomActivity("IU-Celebrity")

        #태 계정 상태 변경
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=music)
        '''
        Status List

        discord.status.online: 온라인 상태로 설정합니다.

        discord.status.offline: 오프라인 상태로 설정합니다.

        discord.status.idle: 자리 비움 상태로 정의합니다.

        discord.status.dnd: 방해 금지 모드로 설정합니다.(빨간색 - 표시)

        discord.status.invisible: 오프라인 상태로 보이게 합니다.( = discord.status.offline)
        -> 오프라인 상태라도 봇은 대답합니다.
        
        
        Activity List

        discord.Game: 게임 하는 중으로 정의합니다.

        discord.Streaming: 방송 하는 중으로 정의합니다. 여기서 제목과 URL 값이 파라미터로 들어갑니다. URL은 트위치 URL이어야합니다.
        
        discord.CustomActivity: 현재 봇에서는 미지원 상태입니다.
        
        discord.Activity: 봇이 활동을 하고 있다고 정의합니다. 여기선 음악 듣는 중, 영상 보는 중이 이에 들어갑니다.
        '''


        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY!")
        guild_list = client.guilds
        for i in guild_list:
            print("서버 ID: {} / 서버 이름: {}".format(i.id, i.name))

    # 봇에 메시가 오면 수행 될 액션
    async def on_message(self, message):
        # sender가 bot이면 반응하지 않기
        if message.author.bot:
            return None

        # message.content = message의 내용
        print("\n\tinput: "+message.content)
        if message.content == "!Arkel":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "Shit"
            # msg에 저장된 내용대로 메시지를 전송
            print("\toutput: "+msg)
            await channel.send(msg)
            return None

        elif message.content == "!상연":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "공부해"
            # msg에 저장된 내용대로 메시지를 전송
            await channel.send(msg)
            print("\toutput: "+msg)
            return None

        elif message.content == "!tagme":
            channel = message.channel
            msg = "<@{}>".format(message.author.id)
            await channel.send(msg)
            print("\toutput: tagged "+str(message.author.id)+", content: "+msg)
            return None

        elif message.content == "!d":
            if message.author.dm_channel:
                await message.author.dm_channel.send("DM 채널이 있어서 그냥 보냈어요!")
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()
                await channel.send("DM 채널이 없어서 만들고 보냈어요!")
            print("\toutput: description to user" + str(message.author.id))

        elif message.content == "!롤할사람":
            channel = message.channel
            sender = message.author
            leagueMember=[]
            fp = open("leagueMember.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueMember.append(line)
            fp.close()

            for i in leagueMember:
                if len(i) < 3:
                    leagueMember.remove(i)

            leagueMemberGathering=0
            fp = open("leagueMemberGathering.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueMemberGathering = int(line)
            fp.close()

            if leagueMemberGathering == 1:
                msg="<@{}>".format(message.author.id)
                msg+="롤팟 이미 구하는중"
                await channel.send(msg)
                return None

            fp = open("leagueList.txt", 'w')
            fp.write(str(sender))
            fp.close()

            leagueList = []
            fp = open("leagueList.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueList.append(line)
            fp.close()

            if sender not in leagueMember:
                leagueMember.append(sender)
                fp = open("leagueMember.txt", 'w')
                for i in leagueMember:
                    fp.write(str(i))
                fp.close()
            msg="롤팟 "+str(len(leagueList))+"/"+str(len(leagueMember))
            await channel.send(msg)
            print("\toutput: " + msg)
            fp = open("leagueMemberGathering.txt", 'w')
            fp.write("1")
            fp.close()


        elif message.content == "!나":
            channel = message.channel
            sender = message.author

            leagueList = []
            fp = open("leagueList.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueList.append(line)
            fp.close()

            leagueMemberGathering=0
            fp = open("leagueMemberGathering.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueMemberGathering = int(line)
            fp.close()

            leagueMember = []
            fp = open("leagueMember.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueMember.append(line)
            fp.close()

            for i in leagueMember:
                if len(i) < 3:
                    leagueMember.remove(i)

            if leagueMemberGathering!=1:
                return None

            if sender in leagueList:
                msg = "<@{}>".format(message.author.id)
                msg += "이미 롤팟에 응답함"
                await channel.send(msg)
                return None

            if sender not in leagueMember:
                leagueMember.append(sender)
                fp = open("leagueMember.txt", 'w')
                for i in leagueMember:
                    fp.write(str(i)+"\n")
                fp.close()

            leagueList.append(sender)
            msg = "롤팟 " + str(len(leagueList)) + "/" + str(len(leagueMember))
            await channel.send(msg)
            print("\toutput: " + msg)

        if message.content == "!롤팟":
            channel = message.channel
            sender = message.author

            leagueList = []
            fp = open("leagueList.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueList.append(line)
            fp.close()

            leagueMemberGathering = 0
            fp = open("leagueMemberGathering.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueMemberGathering = int(line)
            fp.close()

            leagueMember = []
            fp = open("leagueMember.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueMember.append(line)
            fp.close()

            if leagueMemberGathering != 1:
                return None

            msg = "롤팟 " + str(len(leagueList)) + "/" + str(len(leagueMember))
            await channel.send(msg)
            msg = "멤버: "
            await channel.send(msg)
            for member in leagueList:
                await channel.send(str(member))
            print("\toutput: " + msg)

        elif message.content == "!롤팟마감":
            channel = message.channel
            sender = message.author

            leagueList = []
            fp = open("leagueList.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueList.append(line)
            fp.close()

            leagueMemberGathering = 0
            fp = open("leagueMemberGathering.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueMemberGathering = int(line)
            fp.close()

            leagueMember = []
            fp = open("leagueMember.txt", 'r')
            lines = fp.readlines()
            for line in lines:
                leagueMember.append(line)
            fp.close()

            if leagueMemberGathering != 1:
                return None

            fp = open("leagueMemberGathering.txt", 'w')
            fp.write("0")
            fp.close()

            msg = "롤팟 " + str(len(leagueList)) + "/" + str(len(leagueMember))
            await channel.send(msg)
            msg = "멤버: "
            await channel.send(msg)
            for member in leagueList:
                await channel.send(str(member))
            print("\toutput: " + msg)


# 프로그램이 실행되면 가장 먼저 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    f = open("token.txt", 'r')
    line = f.readline()
    client.run(line)