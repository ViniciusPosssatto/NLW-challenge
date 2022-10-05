<template>
	<v-card
		border
		class="mb-2"
		density="compact"
		prepend-avatar="https://randomuser.me/api/portraits/women/10.jpg"
		subtitle="Dias que joga"
		title="Nome da pessoa"
		variant="text"
		>
		<v-card-text>
			Colocar alguma informação aqui
		</v-card-text>

		<template v-slot:actions>
			<v-btn color="primary" variant="text">Estou online</v-btn>

			<v-btn color="primary" variant="text">Alterar game</v-btn>
		</template>
	</v-card>
</template>