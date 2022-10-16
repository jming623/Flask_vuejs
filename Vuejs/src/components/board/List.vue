<template>
	<div>
		<h2>게시판 리스트</h2>
		
		<div class="search-wrap">
			<b-form-input type="text" class="search-input" v-model="keyword" @keyup.enter="fnSearch" />
			<b-button variant="outline-primary" click="fnSearch" class="btn-search">검색</b-button>
		</div>

		<div class="list-wrap">
			<b-table :items="boardList" :fields="tableField" class="tbList">
				<!-- <template #cell(subject)="row">
					<p @click="fnView(`${row.board_no}`)">{{row.subject}}</p>
				</template> -->

				<template #cell(reg_dt)="data">
					{{data.item.reg_dt.substring(0,10)}}
				</template>
				<!-- <colgroup>
					<col width="6%" />
					<col width="*" />
					<col width="10%" />
					<col width="15%" />
				</colgroup> -->
				<!-- <tr>
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
				</tr> -->
			</b-table>
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
			},
			tableField:[
				{key: 'board_no', label:"글번호", sortable: true},
				{key: 'subject', label:"제목", sortable: true},
				{key: 'content', label:"내용", sortable: true},
				{key: 'reg_id', label:"아이디", sortable: true},
				{key: 'reg_dt', label:"날짜", sortable: true},
			]
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
			alert("검색")
			//this.paging.page = 1;
			//this.fnGetList();
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