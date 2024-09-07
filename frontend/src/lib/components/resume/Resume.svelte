<script lang="ts">
	import EducationComponent from "$lib/components/resume/Education.svelte";
	import InterestComponent from "$lib/components/resume/Interest.svelte";
	import LinkComponent from "$lib/components/resume/Link.svelte";
	import PersonalInfoComponent from "$lib/components/resume/PersonalInfo.svelte";
	import PublicationComponent from "$lib/components/resume/Publication.svelte";
	import SkillComponent from "$lib/components/resume/Skill.svelte";
	import AwardComponent from "$lib/components/resume/Award.svelte";
	import CertificateComponent from "$lib/components/resume/Certificate.svelte";
	import CourseComponent from "$lib/components/resume/Course.svelte";
	import LanguageComponent from "$lib/components/resume/Language.svelte";
	import ProfessionalExpComponent from "$lib/components/resume/ProfessionalExp.svelte";
	import ProjectComponent from "$lib/components/resume/Project.svelte";
	import ReferenceComponent from "$lib/components/resume/Reference.svelte";
	import InputText from "$lib/components/InputText.svelte";
	import InputCheckBox from "$lib/components/InputCheckBox.svelte";
	import type { BaseResume } from "$lib/interfaces/resume/Resume";
	import type PersonalInfo from "$lib/interfaces/resume/PersonalInfo";
	import type Link from "$lib/interfaces/resume/Link";
	import type ProfessionalExp from "$lib/interfaces/resume/ProfessionalExp";
	import type Education from "$lib/interfaces/resume/Education";
	import type Course from "$lib/interfaces/resume/Course";
	import type Language from "$lib/interfaces/resume/Language";
	import type Interest from "$lib/interfaces/resume/Interest";
	import type Project from "$lib/interfaces/resume/Project";
	import type Award from "$lib/interfaces/resume/Award";
	import type Reference from "$lib/interfaces/resume/Reference";
	import type Skill from "$lib/interfaces/resume/Skill";
	import type Publication from "$lib/interfaces/resume/Publication";
	import type Certificate from "$lib/interfaces/resume/Certificate";
	import { onMount, tick, type ComponentType } from "svelte";
	import Button from "$lib/components/Button.svelte";
	import Modal from "../Modal.svelte";
	import { getRandomId } from "$lib/utils";

	export const id: number | null = null;
	export let value: BaseResume;

	type ArrayKeys<type> = {
		[key in keyof type]: type[key] extends Array<any> ? key : never;
	}[keyof type];

	type ComponentMapping = {
		key: ArrayKeys<BaseResume>;
		component: ComponentType;
		componentValue: { id?: string | number };
	};

	let isModalHidden: boolean = false;
	let currentSection: ComponentMapping | null = null;
	let backModalClick: (() => void) | null = null;

	const buttons: { [text: string]: ComponentMapping } = {
		...createButton("Professional Experience", "professional_exps", ProfessionalExpComponent),
		...createButton("Link", "links", LinkComponent),
		...createButton("Skill", "skills", SkillComponent),
		...createButton("Award", "awards", AwardComponent),
		...createButton("Certificate", "certificates", CertificateComponent),
		...createButton("Course", "courses", CourseComponent),
		...createButton("Education", "educations", EducationComponent),
		...createButton("Interest", "interests", InterestComponent),
		...createButton("Language", "languages", LanguageComponent),
		...createButton("Project", "projects", ProjectComponent),
		...createButton("Publication", "publications", PublicationComponent),
		...createButton("Reference", "references", ReferenceComponent)
	};

	function createButton(
		text: string,
		key: ArrayKeys<BaseResume>,
		component: ComponentType
	): { [text: string]: ComponentMapping } {
		return {
			[text]: {
				key,
				component,
				componentValue: {}
			}
		};
	}

	const addSection = (section: ComponentMapping) => {
		if (!section || !section.key) return;
		currentSection = section;
		value[section.key] = [...value[section.key], currentSection.componentValue];
	};

	const addCurrentSection = () => {
		if (!currentSection || !currentSection.key) return;
		// Add the next
		value[currentSection.key] = [...value[currentSection.key], {}];
		currentSection.componentValue = {};
	};

	const closeModalClick = (event?: Event) => {
		if (event instanceof KeyboardEvent && event.key !== "Enter") return;
		currentSection = null;
		isModalHidden = true;
	};

	const cancelCurrentSection = () => {
		if (!currentSection || !currentSection.key) return;
		// Remove the last addition
		removeLast();
		resetComponent();
		closeModalClick();
	};

	const removeLast = () => {
		if (currentSection && currentSection.key)
			value[currentSection.key] = [
				...value[currentSection.key].splice(0, value[currentSection.key].length - 1)
			];
	};

	const resetComponent = () => {
		if (!currentSection) return;
		currentSection.componentValue = {};
		currentSection = null;
	};

	$: {
		if (currentSection)
			backModalClick = () => {
				if (currentSection && Object.keys(currentSection.componentValue).length === 1) removeLast();
				resetComponent();
			};
		else backModalClick = null;
	}

	$: {
		if (currentSection && currentSection.key && currentSection.componentValue) {
			// value[currentSection.key] --> value.skills, value.links
			if (value[currentSection.key].length)
				value[currentSection.key] = value[currentSection.key].map((section) => {
					if (
						currentSection &&
						currentSection.componentValue &&
						currentSection.componentValue.id == section.id
					)
						return currentSection.componentValue;
					else return section;
				});
		}
	}
</script>

<section>
	{#if !isModalHidden}
		<Modal closeClick={closeModalClick} backClick={backModalClick}>
			<div>
				<div class="flex justify-center">
					<h2>Add Section</h2>
				</div>
				{#if !currentSection}
					<div class="flex flex-wrap justify-center gap-5">
						{#each Object.entries(buttons) as [text, object], index (index)}
							<Button on:click={() => addSection(object)}>{text}</Button>
						{/each}
					</div>
				{:else}
					<div class="flex flex-col gap-4">
						<svelte:component
							this={currentSection.component}
							bind:value={currentSection.componentValue}
						></svelte:component>
						<div class="flex justify-between">
							<Button on:click={addCurrentSection}>Add</Button>
							<Button on:click={cancelCurrentSection}>Cancel</Button>
						</div>
					</div>
				{/if}
			</div>
		</Modal>
	{/if}
	<InputText label="Resume Name" bind:value={value.title} />
	<InputCheckBox label="Share" bind:value={value.is_shareable}></InputCheckBox>
	<PersonalInfoComponent bind:value={value.personal_info}></PersonalInfoComponent>
	<SkillComponent bind:value={value.skills} config={{ readOnly: true, listLabel: "Skills" }}
	></SkillComponent>


	<div class="fixed bottom-0 right-0 m-9 rounded-lg border-2 bg-slate-100 p-2">
		<Button on:click={() => (isModalHidden = false)}>Add Section</Button>
	</div>
</section>
