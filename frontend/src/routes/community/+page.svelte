 <script lang="ts">
	import { getResumesByMemberId } from '$lib/api/resume';
	import type { Resume } from '$lib/interfaces/resume/Resume';
	import { account } from '$lib/store';
  import { onMount } from 'svelte'; 

  let pdf: any;
  let resume: Resume | null;
  let _html: string;
  onMount(async () => { 
    pdf = await import('html2pdf.js');


   const resumes = await getResumesByMemberId($account.id);
   resume = resumes[0] || null;

   for (const key in resume) {
  if (Object.hasOwnProperty.call(resume, key)) {
    console.log(key, resume[key]);
  }
}

if (resume) {
      _html = `<div style="margin: 10px;">
        <h1>Resume</h1>
        <ul>
          ${Object.entries(resume).map(([key, value]) => {
            return `<li><strong>${key}:</strong> ${formatValue(value)}</li>`;
          }).join('')}
        </ul></div>
      `;
    }
  });
  function formatValue(value: any): string {
    if (typeof value === 'object' && value !== null) {
      return `<ul>${Object.entries(value).map(([key, nestedValue]) => {
        return `<li>${formatValue(nestedValue)}</li>`;
      }).join('')}</ul>`;
    } else {
      return value.toString();
    }
  };
    

    async function toPDF() { 
    
    await pdf.default(_html); 
    } 
    </script>

  <div>{_html}</div>
  <button on:click={toPDF}>test pdf</button>

