<script context="module" lang="ts">
	export interface Config {
		readOnly?: boolean;
		listOnly?: boolean;
		listLabel?: String;
	}
</script>

<script lang="ts">
	import SkillItem from "$lib/components/resume/SkillItem.svelte";
	import type Skill from "$lib/interfaces/resume/Skill";
	import Button from "../Button.svelte";
	import EditModal from "./EditModal.svelte";

	export let value: Skill | Skill[] = {
		name: "",
		description: "",
		skill_level: ""
	};

	export let config: Config = {
		readOnly: false
	};

	let currentSkill: Skill | null = null;

	const handleRemove = (name: string | undefined) => {
		if (Array.isArray(value)) value = value.filter((value) => value.name !== name);
	};

	const handleEdit = (skill: Skill) => {
		currentSkill = { ...skill };
	};
</script>

{#if currentSkill}
	<EditModal component={SkillItem} value={currentSkill}></EditModal>
{/if}
{#if Array.isArray(value) && value.length}
	<div class="flex flex-col">
		{#if config.listLabel}
			<h2>{config.listLabel}</h2>
		{/if}
		{#each value as skill, index (skill.name)}
			<SkillItem bind:value={skill} readOnly={config.readOnly}></SkillItem>
			<div>
				<Button on:click={() => handleEdit(skill)}>Edit</Button>
				<Button on:click={() => handleRemove(skill.name)}>Remove</Button>
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
