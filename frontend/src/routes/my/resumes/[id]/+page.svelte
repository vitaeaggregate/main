<script lang="ts">
	import { checkAccountAndRedirect } from "$lib/store";
	import { page } from "$app/stores";
	import { getResumesByMemberId} from '$lib/api/resume';
	import { onMount } from 'svelte';
	import AppPdf from '../pdf/AppPdf.svelte';
	import Page from '../pdf/Page.svelte';
	import { account } from '$lib/store';
	import type {Resume} from "$lib/interfaces/resume/Resume"
	import { writable } from "svelte/store";
	import type PersonalInfo from "$lib/interfaces/resume/PersonalInfo"
	import Skill from "$lib/components/resume/Skill.svelte";
  
	export const id = writable<number | null>(null);

	$: resumeId = Number($page.params.id);
  
	const loadPage = () => {
	};
  
	checkAccountAndRedirect(loadPage);
  
	let print = false;
	let resume: Resume | null = null;
	let resumePersonalInfo: PersonalInfo | null = null;
	let resumeSkill: Skill[] = []

  
	onMount(async () => {

	if (!$account) return;

	const resumes = await getResumesByMemberId($account.id);
	resume = resumes.find(r => r.id === resumeId);
	resumePersonalInfo = resume?.personal_info;
	resumeSkill = resume?.skills
	console.log(resumeSkill)
	});

	

	$: filteredInfoPersonalInfo = {
    fullName: resumePersonalInfo?.full_name || "",
	jobTitle: resumePersonalInfo?.job_title || "",
	email: resumePersonalInfo?.email || "",
	phoneNumber: resumePersonalInfo?.phone_number || ""
  };

  $: filteredInfoSkill = {
	name: resumeSkill?.name || "",
	description: resumeSkill?.description || "",
	skillLevel: resumeSkill?.skill_level || "",
  }
  
  
	$: htmlStringPersonalInfo = `
	  <h2>Personal Information</h2>
	  <ul>
		<li><strong>Full Name:</strong> ${filteredInfoPersonalInfo.fullName}</li>
		<li><strong>Job Title:</strong> ${filteredInfoPersonalInfo.jobTitle}</li>
		<li><strong>Email:</strong> ${filteredInfoPersonalInfo.email}</li>
		<li><strong>Phone Number:</strong>${filteredInfoPersonalInfo.phoneNumber}</li>
	  </ul>`;

  </script>
  
  <section>
  
	<AppPdf bind:print={print}>
	  <Page>
		<h1>Resume</h1>
		<div style="margin-top: 30px;">{@html htmlStringPersonalInfo} 
			<br />
			<h2>Skills</h2>
			<ul>
				{#each resumeSkill as item}
				<strong>Name:</strong> { item.name } <br />
				<strong>Description:</strong> { item.description } <br />
				<strong>Skill Level:</strong> { item.skillLevel } <br /> <br />
			  {/each}
		  </ul>
	  </Page>
	</AppPdf>
  <br />
	<button on:click={() => (print = true)}>
	  Print
	</button>
  </section>