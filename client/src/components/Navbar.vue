<template>
	<el-row class="navbar">
		<el-col class="nav__logo" :span="3" :offset="1">
			Fisharium
		</el-col>
		<el-col class="navbar__content" :span="17" :offset="3">
			<el-menu
				text-color="grey"
				background-color="transparent"
				mode="horizontal"
				@select="handleSelect"
			>
				<el-menu-item>
					<el-input placeholder="Search"></el-input>
				</el-menu-item>
				<el-menu-item>
					<el-button type="text">Login</el-button>
				</el-menu-item>
				<el-menu-item>
					<el-button type="text">Sign Up</el-button>
				</el-menu-item>

				<el-menu-item>
					<i class="el-icon-shopping-bag-1"></i>
					<el-badge :value="12" class="badge"> </el-badge>
				</el-menu-item>

				<el-menu-item>
					<i class="el-icon-menu" type="primary"></i>
				</el-menu-item>
			</el-menu>
		</el-col>
	</el-row>
</template>

<script>
export default {
	name: "navbar",

	data() {
		return {
			search: "sdf"
		};
	},

	methods: {
		handleSelect(i, j) {}
	}
};
</script>

<style lang="scss" scoped>
.navbar {
	// background-color: rgba(0, 0, 0, 0.8);
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	z-index: 10;
	.nav__logo {
		font-size: 39px;
		margin-top: 10px;
		font-family: "Trade Winds";
		color: #03a9f4;
	}
	.badge {
		top: -10px;
	}
}
.el-menu {
	border-bottom-color: transparent !important;
	display: flex;
	justify-content: flex-end;
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
}

.el-menu-item {
	&:hover {
		background-color: rgba(0, 0, 0, 0.4) !important;
	}
}
</style>
