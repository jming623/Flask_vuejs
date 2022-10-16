<template>
    <div>
        <b-navbar toggleable="lg" type="dark" valiant="info">
            <b-navbar-brand href="#">게시판</b-navbar-brand>

            <b-navbar-toggle target="nav_collapse"/>

            <b-collapse is-nav id="nav_collapse">
                <b-navbar-nav>
                    <b-navbar-item>게시판</b-navbar-item>
                    <b-navbar-item>메뉴2</b-navbar-item>
                    <b-navbar-item>메뉴3</b-navbar-item>
                    <b-navbar-item>메뉴4</b-navbar-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
    
    
    <!-- <header>
        라우터 설정 
        <h1><a href="#" class="logo"><img src="../../assets/logo.png" alt="Vue logo" width="80"></a></h1>
        라우터 설정 후
        <h1><router-link to="/"><img src="../../assets/logo.png" alt="Vue logo" width="80"></router-link></h1>
        <div class="menuWrap">
            <ul class="menu">
                <li><router-link to="/board/list">게시판</router-link></li>
				<li><a href="javascript:;">메뉴2</a></li>
				<li><a href="javascript:;">메뉴3</a></li>
				<li><a href="javascript:;">메뉴4</a></li>
            </ul>
        </div>
    </header> -->
</template>

<script>
export default {
	
}
</script>

<style scoped>
header{width:100%; text-align:center; position:relative; height:120px; border-bottom:1px solid #35495e}
header h1{position:absolute; top:0; left:100px;}
header ul.menu:after{display:block; clear:both; content:'';}
header ul.menu{position:absolute; top:20px; right:50px;}
header ul.menu li{float:left; padding:10px 20px; list-style:none;}

a{text-decoration:none; color:#333;}
</style>
