<script lang="ts">
	import { getResumesByMemberId } from '$lib/api/resume';
	import { onMount } from 'svelte';
	import AppPdf from './AppPdf.svelte'
	import Page from './Page.svelte'
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
</button>