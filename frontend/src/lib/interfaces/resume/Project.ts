export default interface Project {
	id?: number | string;
	// header?: number;
	title?: string;
	sub_title?: string;
	start_date?: string | Date;
	end_date?: string | Date;
	description?: string;
}
