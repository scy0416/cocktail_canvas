<script>
    let { name, image, description, tags } = $props();
</script>

<!-- 카드 시작 -->
<div class="card bg-base-100 m-5 shadow-md">
    <div class="skeleton h-45"></div>
    <div class="card-body">
        <div class="flex gap-2">
            <div class="skeleton h-4 w-10"></div>
            <div class="skeleton h-4 w-10"></div>
        </div>
        <div class="skeleton h-8 w-50"></div>
        <div class="skeleton h-5 w-30"></div>
    </div>
</div>
<!-- 카드 끝 -->