<script>
    import { onMount } from 'svelte';
    export let name;
    export let date;
    export let rating;
    export let review_json;
    let review
    let taste;
    let feeling;
    let atmosphere;
    let appetizer;
    onMount(async () => {
        let tmp = await JSON.parse(review_json);
        taste = tmp['taste'];
        feeling = tmp['feeling'];
        atmosphere = tmp['atmosphere'];
        appetizer = tmp['appetizer'];
        review = tmp["review"];
    });
</script>

<div class="divider"></div>
<!-- 단일 평가 시작 -->
<div class="w-full">
    <!-- 사용자 정보 시작 -->
    <div class="w-full flex items-center">
        <!-- 사용자 이름 시작 -->
        <div>{name}</div>
        <!-- 사용자 이름 끝 -->

        <!-- 등록 날짜 시작 -->
        <div class="ml-2 text-xs">{date}</div>
        <!-- 등록 날짜 끝 -->

        <!-- 점수 정보 시작 -->
        <div class="m-2">[{rating}/10]</div>
        <!-- 점수 정보 끝 -->
    </div>
    <!-- 사용자 정보 끝 -->

    <!-- 평가 글 시작 -->
    <div class="w-full flex flex-col">
        <div>{review}</div>
    </div>
    <!-- 평가 글 끝 -->

    <!-- 평가 정리 표 시작 -->
    <div class="w-full flex">
        <table class="table table-xs table-pin-rows table-pin-cols">
            <thead>
                <tr>
                    <th>맛 평가</th>
                    <th>느낌 평가</th>
                    <th>분위기 평가</th>
                    <th>안주</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{taste}</td>
                    <td>{feeling}</td>
                    <td>{atmosphere}</td>
                    <td>{appetizer}</td>
                </tr>
            </tbody>
        </table>
    </div>
    <!-- 평가 정리 표 끝 -->
</div>
<!-- 단일 평가 끝 -->