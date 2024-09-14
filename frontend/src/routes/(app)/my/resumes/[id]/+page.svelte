<script lang="ts">
  import { page } from "$app/stores";
  import { deleteResume, getResumeById } from "$lib/api/resume";
  import { account } from "$lib/store";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import { goto } from "$app/navigation";
  import Button from "$lib/components/Button.svelte";
  import ResumePreview from "$lib/components/resume/ResumePreview.svelte";
	import EditIcon from "$lib/icons/EditIcon.svelte";
	import DeleteIcon from "$lib/icons/DeleteIcon.svelte";
	import DownloadIcon from "$lib/icons/DownloadIcon.svelte";
	import PlusIcon from "$lib/icons/PlusIcon.svelte";

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
    <div class="flex">
      <div class="bg-white mr-1 w-36 h-24 rounded-xl p-4 items-center">
        <EditIcon /><br />
        <Button on:click={handleResumeEdit}>Edit</Button>
    </div>
    <div class="bg-white mr-1 w-36 h-24 rounded-xl p-4 items-center">
        <DeleteIcon/><br />
      <Button on:click={handleResumeDelete}>Delete</Button>
  </div>
  <div class="bg-white mr-1 w-36 h-24 rounded-xl p-4 items-center">
        <DownloadIcon /><br />
    <Button on:click={handleDownloadPdf}>Download</Button>
</div>
    </div>
    <div class="mt-5 mb-5">
      <ResumePreview bind:resume bind:sectionElement={resumeElement}></ResumePreview>
    </div>
    <div class="flex flex-row justify-center">
    <div class="bg-amber-600 w-12 h-12 rounded-xl shadow-lg p-2.5">
      <Button on:click={handleResumeEdit}><PlusIcon /></Button>
  </div></div>
  </section>
{/if}
