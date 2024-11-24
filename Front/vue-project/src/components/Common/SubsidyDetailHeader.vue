<template>
    <div class='top-div-flex'>
        <v-card class="product-card mt-3 ml-2 pb-3" width="800">
            <div class="card-flex mt-3 ml-7 pt-1">
                <h3> {{subsidy.name}}</h3>
                <!-- <span class="bank-name ml-10 mt-1"> {{ subsidy. }} </span> -->
                <span class="ml-10 mt-1" style="font-size: 14px;"> 
                    <v-icon size="small" style="color: #658EA7;">mdi-heart</v-icon> 찜 개수 {{likesCount}}개
                </span>
            </div>
        </v-card>
        <v-card class="mt-3 ml-2" width="90">
            <v-btn
                class=" heart-center"
                @click="toggleLike"
                variant="text"
                elevation="0"
            >
                <v-icon
                    size="large"
                    style="color: #658EA7;"
                >
                    {{ isLiked ? 'mdi-heart' : 'mdi-heart-outline' }}
                </v-icon>
            </v-btn>
        </v-card>
    </div>
</template>

<script setup>

// props 정의
const props = defineProps({
    subsidy: Object
})

import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useAccountStore } from '@/stores/account';
import { useRoute } from 'vue-router';
const storeAccount = useAccountStore()
const route = useRoute()

// 반응형 상태 정의
const isLiked = ref(false)
const likesCount = ref(props.subsidy.likes_count)

// API 통신을 위한 기본 설정
const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1',
    headers: {
            Authorization: `Token ${storeAccount.token}`
        }
})

// 초기 좋아요 상태 확인
const fetchLikeStatus = async () => {
    try {
        const response = await api.get(`/subsidies/${route.params.id}/`)
        isLiked.value = response.data.is_liked
        likesCount.value = response.data.likes_count
    } catch (error) {
        console.error('좋아요 상태 조회 중 오류 발생:', error)
    }
}

// 컴포넌트 마운트 시 초기 상태 로드
onMounted(() => {
    fetchLikeStatus()
})

// 좋아요 토글 함수
const toggleLike = async () => {
    try {
        const action = isLiked.value ? 'unlike' : 'like'
        const response = await api.put(`/subsidies/${props.subsidy.id}/`, { action })
        
        isLiked.value = response.data.is_liked
        likesCount.value = response.data.likes_count
        console.log('수정 성공')
    } catch (error) {
        console.error('좋아요 처리 중 오류 발생:', error)
    }
}


// <?? 에 대하여>
// 현재 로그인한 유저가 subsidy.like_users라는 속성 배열에 포함되어있다면 속이 꽉찬 하트를 template에 보이고
// icon 버튼 클릭시 찜 취소가 되게 한다
// 반대로, 현재 로그인한 유저가 subsidy.like_users라는 속성 배열에 포함되어있지않다면 속이 빈 (mid-heart-outline)하트를 ui에 보이게 하고
// icon 버튼 클릭시 찜 저장이 되게 한다
// 그리고 db도 해당 변경사항을 반영한다
// 해당변경사항 django rest api 경로는 다음과 같다(http://127.0.0.1:8000/api/v1/subsidies/<int:subsidy_id>/)
// 그러나 django views.py에는 http method GET만 설정되어있다. put을 따로 설정을 해줘야하는지 잘 모르겠다.
// django views.py에 함수는 다음과 같다

// # 보조금 상세 페이지
// @api_view(['GET'])
// @permission_classes([IsAuthenticated])
// def subsidy_detail(request, subsidy_id):

//     # 주어진 ID로 보조금을 조회합니다. 존재하지 않으면 404 에러를 반환합니다.
//     subsidy = get_object_or_404(Subsidy, id=subsidy_id)

//     # 현재 사용자가 이 상품을 좋아요 했는지 확인합니다.
//     is_liked = request.user in subsidy.like_users.all()

//     # 시리얼라이저를 사용하여 데이터 직렬화
//     serializer = SubsidyDetailSerializers(subsidy)
//     # 사용자 정보 직렬화
//     like_users_data = UserSerializer(subsidy.like_users.all(), many=True).data

//     # 좋아요 정보를 추가합니다.
//     response_data = serializer.data
//     response_data['is_liked'] = is_liked
//     response_data['likes_count'] = subsidy.like_users.count()
//     response_data['like_users'] = like_users_data  # 좋아요한 사용자 정보 추가

//     return Response(response_data, status=status.HTTP_200_OK)

// [] 
</script>

<style scoped>
.top-div-flex {
    display: flex;
}

.card-flex {
    display: flex;
}

.heart-center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
}

</style>9