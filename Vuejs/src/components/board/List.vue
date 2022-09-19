<template>
	<div>
		<h2>게시판 리스트</h2>
		
		<div class="searchWrap">
			<input type="text" v-model="keyword" @keyup.enter="fnSearch" />
			<a href="javascript:;" @click="fnSearch" class="btnSearch btn">검색</a>
		</div>

		<div class="listWrap">
			<table class="tbList">
				<colgroup>
					<col width="6%" />
					<col width="*" />
					<col width="10%" />
					<col width="15%" />
				</colgroup>
				<tr>
					<th colspan="1">no</th>
					<th colspan="1">제목</th>
					<th colspan="3">내용</th>
					<th colspan="2">아이디</th>
					<th colspan="2">날짜</th>
				</tr>
				<tr v-for="(row,idx) in boardList" :key="idx">
					<td colspan="1">{{no-idx}}</td>
					<td colspan="1"><a href="javascript:;" @click="fnView(`${row.board_no}`)">{{row.subject}}</a></td>
					<td colspan="3"><a href="javascript:;" @click="fnView(`${row.board_no}`)"></a>{{row.content}}</td>
					<td colspan="2">{{row.reg_id}}</td>
					<td colspan="2">{{row.reg_dt.substring(0,10)}}</td>
				</tr>
				<tr v-if="boardList.length == 0">
					<td colspan="4">데이터가 없습니다.</td>
				</tr>
			</table>
		</div>

		<div class="pagination" v-if="paging.totalCount > 0">
			<a href="javascript:;" @click="fnPage(1)" class="first">&lt;&lt</a>
			<a href="javascript:;" v-if="paging.start_page > 10" @click="fnPage(`${paging.start_page-1}`)" class="prev">&lt;</a>
			<template v-for="(n, index) in paginavigation()">
				<template v-if="paging.page==n">
					<strong :key="index">{{n}}</strong>
				</template>
				<template v-else>
					<a href="javascript:;" @click="fnPage(`${n}`)" :key="index">{{n}}</a>
				</template>
			</template>
			<a href="javascript:;" v-if="paging.total_page > paging.end_page" @click="fnPage(`${paging.end_page+1}`)" class="next">&gt;</a>
			<a href="javascript:;" @click="fnPage(`${paging.total_page}`)" class="last">&gt;&gt;</a>
		</div>

		<div class="btnRightWrap">
			<a @click="fnAdd" class="btn">등록</a>
		</div>
	</div>
</template>

<script>
export default {
	data(){
		return{
			body: ''
			,board_code: 'news'
			,boardList: ''
			,no: '' 
			,paging: ''
			,start_page: ''
			,page: this.$route.query.page ? this.$route.query.page:1
			,keyword: this.$route.query.keyword
			,paginavigation: function(){
				var pageNumber = [];
				var start_page = this.paging.start_page;
				var end_page = this.paging.end_page;
				for (var i = start_page; i <= end_page; i++){
					pageNumber.push(i);
				}
				return pageNumber;
			}
		}
	}
	,mounted(){
		this.getList();
	}
	,methods:{
		fnGetList(){
			this.body = {
				board_code : this.board_code
				,keyword : this.keyword
				,page : this.page
			}
			this.$axios.get('http://127.0.0.1:5000/api/board', {params:this.body})
			.then((res)=>{
				if(res.data.success){
					this.boardList = res.data.result_data;
					this.paging = res.data.paging;
					this.no = this.paging.totalCount - ( (this.paging.page - 1) * this.paging.ipp );
				}else{
					alert("실행중 실패했습니다.\n다시 이용해 주세요.");
				}
			}).catch((err)=>{
				console.log(err);
			})
		}
		,fnAdd(){
			this.$router.push("./write");
		}		
		,fnSearch(){
			this.paging.page = 1;
			this.fnGetList();
		}
		,getList(){
			this.$axios.get('http://127.0.0.1:5000/api/board/')
			.then((res)=>{
				if(res.data.result_code == 'success'){
					console.log(res.data.result_data)
					this.boardList = res.data.result_data;
					alert("Flask서버와 통신성공")
				}else{
					alert("실행중 실패했습니다.\n다시 이용해 주세요.");
				}
			}).catch((err)=>{
				console.log(err);
			})
		}
		,fnPage(n){
			if(this.page != n){
				this.page = n;
				this.fnGetList();
			}
		}
		,fnView(num){
			this.body.num = num;
			this.$router.push({
				path:'./view', query:this.body
			});
		}
	}
}
</script>

<style scoped>
	.searchWrap{border:1px solid #888; border-radius:5px; text-align:center; padding:20px 0; margin-bottom:40px;}
	.searchWrap input{width:60%; height:36px; border-radius:3px; padding:0 10px; border:1px solid #888;}
	.searchWrap .btnSearch{display:inline-block; margin-left:10px;}
	.tbList th{border-top:1px solid #888;}
	.tbList th, .tbList td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbList td.txt_left{text-align:left;}
	.btnRightWrap{text-align:right; margin:10px 0 0 0;}

	.pagination{margin:20px 0 0 0; text-align:center;}
	.first, .prev, .next, .last{border:1px solid #666; margin:0 5px;}
	.pagination span{display:inline-block; padding:0 5px; color:#333;}
	.pagination a{text-decoration:none; display:inline-blcok; padding:0 5px; color:#666;}
</style>
