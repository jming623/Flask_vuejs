<template>
    <div>
		<h1>게시판 상세보기</h1>

		<div class="AddWrap">
			<form>
				<table class="tbAdd">
					<colgroup>
						<col width="15%" />
						<col width="*" />
					</colgroup>
					<tr>
						<th>제목</th>
						<td>{{subject}}</td>
					</tr>
					<tr>
						<th>내용</th>
						<td class="txt_cont" v-html="cont"></td>
					</tr>
				</table>
			</form>
		</div>

		<div class="btnWrap">
			<a href="javascript:;" @click="fnList" class="btn">목록</a>
            <a href="javascript:;" @click="fnMod" class="btnAdd btn">수정</a>
            <a v-if="num" href="javascript:;" @click="fnDel" class="btnAdd btn">삭제</a>
		</div>	
	</div>
</template>
<script>
    export default{
        data(){
            return{
                body: this.$route.query
                ,subject:''
			    ,cont:''
			    ,view:''
			    ,num:this.$route.query.num
            }
        }
        ,mounted(){
            this.fnGetView();
        }
        ,methods:{
            fnGetView(){
                this.$axios.get("http://localhost:3000/api/board/"+this.body.num, {params:this.body})
                .then((res)=>{
                    console.log(res)
                    this.view = res.data.view[0];
                    this.subject = this.view.subject;
                    this.cont = this.view.cont.replace(/(\n)/g,'<br/>');//\n마다 한칸 띄어주는 용도인듯
                })
                .catch((err)=>{
                    console.log(err);
                })
            }
            ,fnList(){
                delete this.body.num;
                this.$router.push({path:'./list', query:this.body});
            }
            ,fnMod(){
                this.$router.push({path:'./write', query:this.body});
            }
            ,fnDel(){
                if(confirm("정말 삭제하시겠습니까?")){
                    this.$axios.delete('http://localhost:3000/api/board', {params:this.body})
                    .then((res)=>{
                        alert("성공적으로 게시글이 삭제되었습니다.");
                        this.fnList();
                    })
                    .catch((err)=>{
                    console.log(err);
                    })
                }   
            }
        }
    }
</script>

<style scoped>
	.tbAdd{border-top:1px solid #888;}
	.tbAdd th, .tbAdd td{border-bottom:1px solid #eee; padding:5px 0; }
	.tbAdd td{padding:10px 10px; box-sizing:border-box; text-align:left;}
	.tbAdd td.txt_cont{height:300px; vertical-align:top;}
	.btnWrap{text-align:center; margin:20px 0 0 0;}
	.btnWrap a{margin:0 10px;}
	.btnAdd {background:#43b984}
	.btnDelete{background:#f00;}
</style>