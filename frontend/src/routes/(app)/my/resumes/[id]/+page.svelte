<script lang="ts">
  import { page } from "$app/stores";
  import { deleteResume, getResumeById } from "$lib/api/resume";
  import { account } from "$lib/store";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import { goto } from "$app/navigation";
  import Button from "$lib/components/Button.svelte";
  import ResumePreview from "$lib/components/resume/ResumePreview.svelte";

  let resume: Resume | null = null;
  let resumeElement: HTMLElement | null = null;

  const loadResume = async () => (resume = await getResumeById($page.params.id));

  const handleResumeDelete = () => {
    if (!resume) return;
    deleteResume(resume.id);
    goto("/my/page");
  };

  const handleResumeEdit = () => {
    if (!resume) return;
    goto(`/my/resumes/${resume.id}/edit`);
  };

  const handleDownloadPdf = async () => {
    if (!resume || !resumeElement) throw console.log("Resume not loaded.");

    const body = resumeElement.innerHTML;

    const response = await fetch("./resumes", {
      method: "POST",
      headers: {
        "Content-Type": "applications/json"
      },
      body: JSON.stringify({ body })
    });

    if (!response.ok) throw console.log("Fetch error");

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const invisibleLink = document.createElement("a");
    invisibleLink.href = url;
    invisibleLink.download = "resume.pdf";
    invisibleLink.click();
    URL.revokeObjectURL(url);
  };

  $: if ($account && $page.params.id) loadResume();
</script>

{#if $account && $page.params.id && resume}
  <section>
    <div class="flex gap-3">
      <Button on:click={handleResumeEdit}>Edit</Button>
      <Button on:click={handleResumeDelete}>Delete</Button>
      <Button on:click={handleDownloadPdf}>Download</Button>
    </div>
    <div class="p-5">
      <ResumePreview bind:resume bind:sectionElement={resumeElement}></ResumePreview>
    </div>
  </section>
{/if}
