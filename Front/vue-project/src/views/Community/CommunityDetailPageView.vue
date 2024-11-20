<template>
    <br>
    <v-card class="mt-4" width="900" height="500" elevation="2">
        <card-head>
            <p class="mt-2 pl-4">title</p>
        </card-head>
        <hr style="color: #767676;" class="mt-3">
        <div class="card-user-info mt-2 pl-4" style="color: #767676;">
            <span>id님</span>
            <span> 수정날짜</span>
            <div>
                <v-btn @click="dialog = true">수정하기<v-icon>mdi-pencil</v-icon></v-btn>
                <!-- 모달창 -->
                <v-dialog v-model="dialog" max-width="500">
                    <v-card max-width="400" prepend-icon="mdi-update"
                        text="Your application will relaunch automatically after the update is complete."
                        title="Update in progress">
                        <template v-slot:actions>
                            <!-- 이 슬롯은 카드 하단에 버튼과 같은 액션 요소를 추가하는 데 사용 -->
                            <v-btn class="ms-auto" text="Ok" @click="dialog = false"></v-btn>
                        </template>
                    </v-card>
                </v-dialog>
            </div>
            <a href="#"> 삭제하기<v-icon>mdi-trash-can-outline</v-icon></a>
        </div>
        <card-content>
            <p class="mt-4 pl-4">content</p>
        </card-content>
        <hr style="color: #767676;" class="mt-3">
        <div class='comment-input' style="display: flex; align-content: center;">
            <v-text-field class="mt-1 pl-3" style="width: 70%;" density="compact" placeholder="댓글 달기"
                prepend-inner-icon="mdi-comment-text-outline"></v-text-field>
            <v-btn class="mb-8 ml-2 mt-1" color="#658EA7" size="large" variant="tonal">
                작성
            </v-btn>
        </div>
        <div class='comment-list'>
            <p>댓글 목록</p>
            <p> 님 좀 짱인듯<span>
                    <v-btn density="compact" icon="mdi-pencil"></v-btn>
                    <v-btn density="compact" icon="mdi-trash-can-outline"></v-btn>
                </span>
            </p>
        </div>
    </v-card>
    <a href="#">이전 페이지로 돌아가기<v-icon>mdi-chevron-left</v-icon></a>
</template>

<script setup>
const dialog = ''
</script>

<style scoped>
.card-user-info {
    font-size: 15px,

}
</style>