<script context="module" lang="ts">
	export interface Config {
		readOnly?: boolean;
		listLabel?: String;
	}
</script>

<script lang="ts">
	import SkillItem from "$lib/components/resume/SkillItem.svelte";
	import type Skill from "$lib/interfaces/resume/Skill";
	import Button from "$lib/components/Button.svelte";
	import Modal from "$lib/components/Modal.svelte";
	import EditModal from "$lib/components/resume/EditModal.svelte";

	export let value: Skill | Skill[] = {
		name: "",
		description: "",
		skill_level: ""
	};

	export let config: Config = {
		readOnly: false
	};

	let currentSkill: Skill | null = null;

	const handleRemove = (id: string | number) => {
		if (Array.isArray(value)) value = [...value.filter((value) => value.id !== id)];
	};

	const handleEdit = (skill: Skill) => {
		currentSkill = skill;
	};

	const closeModalClick = () => {
		currentSkill = null;
	};

	$: {
		if (Array.isArray(value) && currentSkill) {
			for (let skill of value)
				if (skill.id === currentSkill.id) {
					skill = currentSkill;
					value = [...value, skill];
				}
		}
	}
</script>

{#if currentSkill}
	<Modal closeClick={closeModalClick}>
		<EditModal component={SkillItem} bind:value={currentSkill} {closeModalClick}></EditModal>
	</Modal>
{/if}
{#if Array.isArray(value) && value.length}
	<div class="flex flex-col">
		{#if config.listLabel}
			<h2>{config.listLabel}</h2>
		{/if}
		{#each value as skill (skill.id)}
			<SkillItem bind:value={skill} readOnly={config.readOnly}></SkillItem>
			<div>
				<Button on:click={() => handleEdit(skill)}>Edit</Button>
				<Button
					on:click={() => {
						if (skill.id) handleRemove(skill.id);
					}}>Remove</Button
				>
			</div>
			<hr />
		{/each}
	</div>
{:else if !Array.isArray(value)}
	<div class="flex flex-col">
		<h2>Skill</h2>
		<SkillItem bind:value readOnly={config.readOnly}></SkillItem>
	</div>
{/if}
