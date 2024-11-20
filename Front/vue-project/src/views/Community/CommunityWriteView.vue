<template>
    <v-card width="900" height="400" elevation="4">
        <card-title>
            <v-text-field placeholder="제목을 작성해주세요." variant="solo"></v-text-field>
        </card-title>
        <hr style="color: #767676;">
        <card-content>
            <v-text-field class="v-text-field2" placeholder="본문을 작성해주세요." ></v-text-field>
        </card-content>
        <div>
            <p>키워드를 선택해주세요.</p>
            <v-btn v-for="(btn, index) in buttons" :key="index" :class="{ 'active-button': selectedButton === index }"
                @click="selectButton(index)" density="compact">
                {{ btn.caption }}
            </v-btn>
        </div>
    </v-card>
    <v-btn class="mt-2" density="compact">글 올리기</v-btn>
</template>

<script setup>
import { ref } from 'vue';

// Define the buttons with captions
const buttons = ref([
    { caption: '적금' },
    { caption: '예금' },
    { caption: '지원금' }
]);

// Reactive property to track the selected button index
const selectedButton = ref(null);

// Function to select a button
const selectButton = (index) => {
    // Update the selected button index
    selectedButton.value = index;
};
</script>


<style scoped>
.v-text-field2 {
    height: 200px;
}

.active-button {
    background-color: #658EA7; 
    color: white;
}

</style>