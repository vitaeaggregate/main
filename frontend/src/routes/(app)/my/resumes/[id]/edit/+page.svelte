<script lang="ts">
  import { goto } from "$app/navigation";
  import { page } from "$app/stores";
  import { getResumeById, updateResume } from "$lib/api/resume";
  import ResumeComponent from "$lib/components/resume/Resume.svelte";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import { account } from "$lib/store";
  import Toasts from "$lib/components/Toasts.svelte";
  import { addToast } from "$lib/store";
  import Button from "$lib/components/Button.svelte";

  let resume: Resume | null = null;

  let message = "One or more fields are incorrect!";
  let type = "error";
  let dismissible = true;
  let timeout = 3000;

  const loadResume = async () => {
    if (!$account || !$page.params.id) return;
    resume = await getResumeById(Number($page.params.id));
  };

  const handleSaveClick = async () => {
    try {
      if (!$account || !resume) return;
      const updatedResume: Resume = await updateResume(resume);
      resume = updatedResume;
      if (resume) goto(`/my/resumes/${resume?.id}`);
    } catch {
      addToast({
        message,
        type,
        dismissible,
        timeout
      });
    }
  };

  const handleCancelClick = () => {
    if (!resume) return;

    goto(`/my/resumes/${resume.id}`);
  };

  $: if ($page.params.id && $account) loadResume();
</script>

<section>
  <Toasts />
  <h1>Edit Resume</h1>
  {#if resume}
  <div class="flex flex-row gap-3 my-4">
    <Button on:click={handleCancelClick} style="cancel">Cancel</Button>
    <Button on:click={handleSaveClick} style="add">Save</Button></div>
    <ResumeComponent bind:value={resume}></ResumeComponent><br />
  {/if}
</section>
