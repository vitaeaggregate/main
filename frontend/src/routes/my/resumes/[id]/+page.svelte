<script lang="ts">
	import { checkAccountAndRedirect } from "$lib/store";
	import { page } from "$app/stores";
	import { getResumesByMemberId} from '$lib/api/resume';
	import { onMount } from 'svelte';
	import AppPdf from '../pdf/AppPdf.svelte';
	import Page from '../pdf/Page.svelte';
	import { account } from '$lib/store';
	import type PersonalInfo from "$lib/interfaces/resume/PersonalInfo";
	import type {Resume} from "$lib/interfaces/resume/Resume"
	import { writable } from "svelte/store";
  
	export const id = writable<number | null>(null);

	$: resumeId = Number($page.params.id);
  
	const loadPage = () => {
	};
  
	checkAccountAndRedirect(loadPage);
  
	let print = false;
	let resume: Resume | null = null;
  
	onMount(async () => {

		if (!$account) return;

	const resumes = await getResumesByMemberId($account.id);
	resume = resumes.find(r => r.id === resumeId)?.personal_info;
	});

	$: filteredInfo = {
    fullName: resume?.full_name || "",
	jobTitle: resume?.job_title || "",
	email: resume?.email || "",
	phoneNumber: resume?.phone_number || ""
  };
  
	$: htmlStringPersonalInfo = `
	  <h2>Personal Information</h2>
	  <ul>
		<li><strong>Full Name:</strong> ${filteredInfo.fullName}</li>
		<li><strong>Job Title:</strong> ${filteredInfo.jobTitle}</li>
		<li><strong>Email:</strong> ${filteredInfo.email}</li>
		<li><strong>Phone Number:</strong>${filteredInfo.phoneNumber}</li>
	  </ul>
	`;

  </script>
  
  <section>
  
	<AppPdf bind:print={print}>
	  <Page>
		<div style="margin-top: 30px;">{@html htmlStringPersonalInfo}</div>
	  </Page>
	</AppPdf>
  
	<button on:click={() => (print = true)}>
	  Print
	</button>
  </section>