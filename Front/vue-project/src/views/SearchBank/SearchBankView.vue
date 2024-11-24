<template>

                <h1 class="title" style="color:#658EA7;">내 집 주변 은행 찾기</h1>
                <div class="flex">
                    <v-form>
                        <div class="select-container" style="max-width: 700px; margin: auto;">
                            <v-select v-model="selectedCity" label="광역시/도" :items="location1" variant="solo"></v-select>
                            <v-select v-model="selectedDistrict" label="시/군/구" :items="location2"
                                variant="solo"></v-select>
                            <v-select v-model="selectedBank" label="은행명" :items="bankname" variant="solo"></v-select>
                            <v-btn @click="searchBanks" style="height: 56px; color: #658EA7;  font-size: 18px;"
                                rounded="small"><v-icon>mdi-map</v-icon>찾기</v-btn>
                        </div>
                    </v-form>

                    <v-card height="400px" width="700px" style="margin: auto;" hover>
                        <KakaoMap :searchParams="searchParams" />
                    </v-card>
                </div>

</template>

<script setup>
import KakaoMap from '@/components/Bank/KakaoMap.vue';

const location1 = [
    '서울특별시',
    '부산광역시',
    '대구광역시',
    '인천광역시',
    '광주광역시',
    '대전광역시',
    '울산광역시',
    '세종특별자치시',
    '경기도',
    '강원특별자치도',
    '충청북도',
    '충청남도',
    '전라북도',
    '전라남도',
    '경상북도',
    '경상남도',
    '제주특별자치도'
] // 예시 데이터


const location2 = ref([]);
const location2Data = {
    '서울특별시': ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'],
    '부산광역시': ['중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구', '연제구', '수영구', '사상구', '기장군'],
    '대구광역시': ['중구', '동구', '서구', '남구', '북구', '수성구', '달서구', '달성군'],
    '인천광역시': ['중구', '동구', '미추홀구', '연수구', '남동구', '부평구', '계양구', '서구', '강화군', '옹진군'],
    '광주광역시': ['동구', '서구', '남구', '북구', '광산구'],
    '대전광역시': ['동구', '중구', '서구', '유성구', '대덕구'],
    '울산광역시': ['중구', '남구', '동구', '북구', '울주군'],
    '세종특별자치시': ['세종특별자치시'],
    '경기도': ['수원시', '고양시', '용인시', '성남시', '부천시', '화성시', '안산시', '남양주시', '안양시', '평택시', '시흥시', '파주시', '의정부시', '김포시', '광주시', '광명시', '군포시', '하남시', '오산시', '양주시', '이천시', '구리시', '안성시', '포천시', '의왕시', '여주시', '양평군', '동두천시', '과천시', '가평군', '연천군'],
    '강원특별자치도': ['춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '홍천군', '횡성군', '영월군', '평창군', '정선군', '철원군', '화천군', '양구군', '인제군', '고성군', '양양군'],
    '충청북도': ['청주시', '충주시', '제천시', '보은군', '옥천군', '영동군', '증평군', '진천군', '괴산군', '음성군', '단양군'],
    '충청남도': ['천안시', '공주시', '보령시', '아산시', '서산시', '논산시', '계룡시', '당진시', '금산군', '부여군', '서천군', '청양군', '홍성군', '예산군', '태안군'],
    '전라북도': ['전주시', '군산시', '익산시', '정읍시', '남원시', '김제시', '완주군', '진안군', '무주군', '장수군', '임실군', '순창군', '고창군', '부안군'],
    '전라남도': ['목포시', '여수시', '순천시', '나주시', '광양시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군', '장흥군', '강진군', '해남군', '영암군', '무안군', '함평군', '영광군', '장성군', '완도군', '진도군', '신안군'],
    '경상북도': ['포항시', '경주시', '김천시', '안동시', '구미시', '영주시', '영천시', '상주시', '문경시', '경산시', '군위군', '의성군', '청송군', '영양군', '영덕군', '청도군', '고령군', '성주군', '칠곡군', '예천군', '봉화군', '울진군', '울릉군'],
    '경상남도': ['창원시', '진주시', '통영시', '사천시', '김해시', '밀양시', '거제시', '양산시', '의령군', '함안군', '창녕군', '고성군', '남해군', '하동군', '산청군', '함양군', '거창군', '합천군'],
    '제주특별자치도': ['제주시', '서귀포시']
};

const bankname = ['국민은행', '신한은행', '우리은행']; // 예시 데이터
import { ref, watch } from 'vue'

const selectedCity = ref('');
const selectedDistrict = ref('');
const selectedBank = ref('');


// props할 데이터
const searchParams = ref({
    city: '',
    district: '',
    bank: ''
});

watch(selectedCity, (newCity) => {
    location2.value = location2Data[newCity] || [];
    selectedDistrict.value = ''; // 도시가 변경되면 구/군 선택을 초기화
});


const searchBanks = () => {
    searchParams.value.city = selectedCity.value;
    searchParams.value.district = selectedDistrict.value;
    searchParams.value.bank = selectedBank.value;
    // console.log(searchParams.value);
};
</script>

<style scoped>
.select-container {
    display: flex;
    flex-direction: row;
    gap: 10px;
    /* margin-top: 30px; */

}

h1 {
    text-align: center;
}

.flex {
    display: flex;
    flex-direction: column;
    /* margin: auto; */
    /* align-items: center; */

}

.title {

    /* margin-left: 50px; */
    margin-bottom: 40px;
    margin-top: 20px;

}
</style>