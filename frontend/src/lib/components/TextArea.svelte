<script lang="ts">
  export let label: string | null = "Text area";
  export let placeholder: string | null = label;
  export let value: string = "";
  export let required: boolean = false;
</script>

<label class="flex flex-col">
  {required ? "*" : ""}
  {label ? label + ":" : ""}
  <textarea {placeholder} bind:value class="h-3/6 border-2 p-1"></textarea>
</label>
