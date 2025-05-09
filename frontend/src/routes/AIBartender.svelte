<script>
    import UserChat from '../components/UserChat.svelte';
    import BotChat from '../components/BotChat.svelte';
    import CocktailCard from '../components/CocktailCard.svelte';
</script>

<!-- 채팅 대화 박스 시작 -->
<div class="ml-5 mr-5 md:ml-50 md:mr-50 h-100">
    <div class="w-full p-3 h-full overflow-auto outline outline-gray-200 outline-2 rounded-box">
        <UserChat message="유저 메시지" />
        <BotChat message="봇 메시지" />
    </div>
</div>
<!-- 채팅 대화 박스 끝 -->

<!-- 입력창 시작 -->
<div class="join ml-5 mr-5 md:ml-50 md:mr-50 flex shadow-sm">
    <input type="text" placeholder="입력창" class="w-full input join-item">
    <button class="btn join-item">전송</button>
</div>
<!-- 입력창 끝 -->

<!-- 추천 칵테일 표시 창 시작 -->
<div class="grid grid-cols-4 md:ml-45 md:mr-45">
    <CocktailCard name="COCKTAIL_NAME" image="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp" description="DESCRIPTION" tags={["TAG1", "TAG2"]} />
    <CocktailCard name="COCKTAIL_NAME" image="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp" description="DESCRIPTION" tags={["TAG1", "TAG2"]} />
    <CocktailCard name="COCKTAIL_NAME" image="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp" description="DESCRIPTION" tags={["TAG1", "TAG2"]} />
    <CocktailCard name="COCKTAIL_NAME" image="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp" description="DESCRIPTION" tags={["TAG1", "TAG2"]} />
</div>
<!-- 추천 칵테일 표시 창 끝 -->