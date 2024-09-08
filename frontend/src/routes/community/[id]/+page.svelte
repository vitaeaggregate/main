<!-- <script lang="ts">
	import { getResumesByMemberId } from '$lib/api/resume';
	import { onMount } from 'svelte';
	import AppPdf from './AppPdf.svelte'
	import Page from './[id]/Page.svelte'
	import { account } from '$lib/store';
	import Resume from '$lib/components/resume/Resume.svelte';

	let print = false
    let resume: Resume[];

    onMount(async () => { 
        const resumes = await getResumesByMemberId($account.id);
        resume = resumes[0] || null;

    })

  let personalInfo = {
    id: 26,
    full_name: 'Blood return stand threat gun whether collection. ...ain site order. Fire study shoulder effect leave.',
    job_title: 'Middle range other best at admit or skill. Detail ... purpose sport. Hotel traditional through return.',
    email: 'isaacrowland@example.net',
    phone_number: '516-377-1526x91',
  };

  $: filteredInfo = {
    full_name: personalInfo.full_name,
    job_title: personalInfo.job_title,
    email: personalInfo.email ? `<strong>Email:</strong> ${personalInfo.email}` : '',
    phone_number: personalInfo.phone_number ? `<strong>Phone:</strong> ${personalInfo.phone_number}` : '',
  };

  $: htmlStringPersonalInfo = `
    <h2>Personal Information</h2>
    <ul>
      <li><strong>Full Name:</strong> ${filteredInfo.full_name}</li>
      <li><strong>Job Title:</strong> ${filteredInfo.job_title}</li>
      ${filteredInfo.email && `<li>${filteredInfo.email}</li>`}
      ${filteredInfo.phone_number && `<li>${filteredInfo.phone_number}</li>`}
    </ul>
  `;

</script>

<AppPdf bind:print={print}>
	<Page>
        <div style="margin-top: 30px;">{@html htmlStringPersonalInfo}</div>
	</Page>
</AppPdf>

<button on:click={() => (print=true)}>
	Print
</button> -->

<script lang="ts">
	import type { Comment } from "$lib/interfaces/resume/Comment";
	import { writable } from "svelte/store";
	import { getCommentsByMemberIdByResumeId } from "$lib/api/comment";
	import { getResumesByMemberId } from "$lib/api/resume";
	import { account, checkAccountAndRedirect} from "$lib/store";
	import type { Resume } from "$lib/interfaces/resume/Resume";
	import { page } from "$app/stores";
	import NewComment from "$lib/components/resume/comment.svelte";
	import AppPdf from './AppPdf.svelte'
	import Page from './Page.svelte'

	export const id = writable<number | null>(null);

	$: resumeId = Number($page.params.id);

	let print = false
	let resumes: Resume[] | null = null;
	let resumesComments: { [resumeId: number]: Comment[] } = {};

	const loadPage = async () => {
		if (!$account) return;

		const resume = await getResumesByMemberId($account.id);
		
        resumes = resume[resumeId] || null;

		for (let resume of resumes) {
			const comments = await getCommentsByMemberIdByResumeId($account.id, resume.id);
			resumesComments[resume.id] = comments;
		}
	};

	checkAccountAndRedirect(loadPage);

	let personalInfo = {
    id: 26,
    full_name: 'Blood return stand threat gun whether collection. ...ain site order. Fire study shoulder effect leave.',
    job_title: 'Middle range other best at admit or skill. Detail ... purpose sport. Hotel traditional through return.',
    email: 'isaacrowland@example.net',
    phone_number: '516-377-1526x91',
  };

  $: filteredInfo = {
    full_name: personalInfo.full_name,
    job_title: personalInfo.job_title,
    email: personalInfo.email ? `<strong>Email:</strong> ${personalInfo.email}` : '',
    phone_number: personalInfo.phone_number ? `<strong>Phone:</strong> ${personalInfo.phone_number}` : '',
  };

  $: htmlStringPersonalInfo = `
    <h2>Personal Information</h2>
    <ul>
      <li><strong>Full Name:</strong> ${filteredInfo.full_name}</li>
      <li><strong>Job Title:</strong> ${filteredInfo.job_title}</li>
      ${filteredInfo.email && `<li>${filteredInfo.email}</li>`}
      ${filteredInfo.phone_number && `<li>${filteredInfo.phone_number}</li>`}
    </ul>
  `;
</script>

<main>
	<h1>Community</h1>
	<br />
	<div class="test-div flex justify-center">
		<div class="h-3/5 w-4/5 overflow-y-auto bg-gray-200 p-6">
			{#if resumes}
			<AppPdf bind:print={print}>
				<Page>
					<div style="margin-top: 30px;">{@html htmlStringPersonalInfo}</div>
				</Page>
			</AppPdf>
			<br />
			<button on:click={() => (print=true)}>
				Print
			</button>
			{/if}
		</div>
	</div>
	<br /><br />
	<h2>Comments</h2>
	<div class="flex justify-center">
		<div class="h-3/5 w-4/5 overflow-y-auto p-6">
			<ul class="flex flex-col gap-5 p-5">
				{#each Object.entries(resumesComments) as [id, comments]}
					{#if +id === resumeId}
						<h2>Resume ID: {id}</h2>
						<ul>
							{#each comments as comment}
								<li>{comment.description}</li>
							{/each}
						</ul>{/if}
				{/each}
			</ul>
		</div>
	</div>
	<h3>New comment</h3>
	<NewComment></NewComment>
</main>
