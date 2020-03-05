<template>
	<div class="footer">
		<div class="logo">
			Fishaium
		</div>
		<el-row>
			<el-col :span="12">
				<ul class="footer-list">
					<li class="footer-list__item">
						<a class="footer-list__link">company</a>
					</li>
					<li class="footer-list__item">
						<a class="footer-list__link">contact us</a>
					</li>
					<li class="footer-list__item">
						<a class="footer-list__link">carrers</a>
					</li>
					<li class="footer-list__item">
						<a class="footer-list__link">privacy policy</a>
					</li>
					<li class="footer-list__item">
						<a class="footer-list__link"> terms</a>
					</li>
				</ul>
			</el-col>
			<el-col :span="12">
				<div class="footer-copy">
					<p>
						Lorem ipsum dolor sit amet consectetur adipisicing elit.
						Labore autem eligendi eum, officia ratione eaque unde
						aliquid in quae! Ipsa fugiat ut necessitatibus velit
						enim quam qui eum minima aspernatur!
					</p>
				</div>
			</el-col>
		</el-row>
	</div>
</template>

<script>
export default {
	name: "Footer"
};
</script>

<style lang="scss" scoped>
.footer {
	padding: 4rem 6rem;
	background-color: #333;
	color: white;
	font-size: 1.6rem;
}
.logo {
	text-align: center;
	font-size: 4rem;
	margin-bottom: 5rem;
	font-family: "Trade Winds";
	color: #03a9f4;
}

.footer-list {
	list-style: none;
	&__item {
		display: inline-block;
		margin-right: 2rem;
	}
	&__link {
		text-decoration: none;
		text-transform: uppercase;
		cursor: pointer;
		&::after {
			content: "";
			display: block;
			width: 100%;
			height: 2px;
			background: blue;
			transform: scale(0);
			transition: all 0.4s;
		}
		&:hover::after {
			transform: scale(1);
		}
	}
}

.footer-copy {
	padding: 0 3rem;
}
</style>
