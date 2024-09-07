<script lang="ts">
  import { getResumesByMemberId, getResumesByResumeId } from '$lib/api/resume';
  import { onMount } from 'svelte';
  import AppPdf from './AppPdf.svelte';
  import Page from './Page.svelte';
  import { account } from '$lib/store';

  let print = false;
  let resume: Resume | null = null;

  onMount(async () => {
    const resumes = await getResumesByMemberId($account.id);
    resume = resumes[0] || null;
    console.log(resume);

  });

  function getPersonalInfo(resume: Resume): {
    fullName: string;
    jobTitle: string;
    email?: string;
    phoneNumber?: string;
  } {
    return {
      fullName: resume.personal_info.full_name,
      jobTitle: resume.personal_info.job_title,
      email: resume.personal_info.email,
      phoneNumber: resume.personal_info.phone_number,
    };
  }

  let personalInfo: {
    fullName: string;
    jobTitle: string;
    email?: string;
    phoneNumber?: string;
  } = { fullName: '', jobTitle: '' };

  $: personalInfo = resume ? getPersonalInfo(resume) : {}; 

  $: filteredInfo = {
    full_name: personalInfo.fullName,
    job_title: personalInfo.jobTitle,
    email: personalInfo.email ? `<strong>Email:</strong> ${personalInfo.email}` : '',
    phone_number: personalInfo.phoneNumber
      ? `<strong>Phone:</strong> ${personalInfo.phoneNumber}`
      : '',
  };

  $: htmlStringPersonalInfo = `
    <h2>Personal Information</h2>
    <ul>
      <li><strong>Full Name:</strong> ${filteredInfo.full_name}</li>
      <li><strong>Job Title:</strong> ${filteredInfo.jobTitle}</li>
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