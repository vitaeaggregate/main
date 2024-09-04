<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";
	import TextArea from "$lib/components/TextArea.svelte";

	export let value = {};

	let inputName: string = "";
	let inputDescription: string = "";
	let inputSkillLevel: string = "";

	$: value = {
		name: inputName,
		description: inputDescription,
		skill_level: inputSkillLevel
	};
</script>

<div class="flex flex-col">
	<h2>Skills</h2>
	<InputText label="Name" bind:value={inputName} />
	<TextArea label="Description" bind:value={inputDescription} />
	<InputText label="Skill Level" bind:value={inputSkillLevel} />
</div>
