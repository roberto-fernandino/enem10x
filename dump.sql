--
-- PostgreSQL database dump
--

-- Dumped from database version 14.9 (Ubuntu 14.9-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.9 (Ubuntu 14.9-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	materiais	conteudo
7	materiais	materia
8	materiais	nivel
9	materiais	tipo
10	materiais	submateria
11	materiais	questao
12	materiais	provarespondida
13	materiais	provacompleta
14	usuarios	account
15	usuarios	mediageral
16	materiais	questaorespondida
17	materiais	simulado
18	usuarios	notas
19	usuarios	aluno
20	usuarios	turma
21	usuarios	professor
22	materiais	opcaoimagem
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add conteudo	6	add_conteudo
22	Can change conteudo	6	change_conteudo
23	Can delete conteudo	6	delete_conteudo
24	Can view conteudo	6	view_conteudo
25	Can add materia	7	add_materia
26	Can change materia	7	change_materia
27	Can delete materia	7	delete_materia
28	Can view materia	7	view_materia
29	Can add nivel	8	add_nivel
30	Can change nivel	8	change_nivel
31	Can delete nivel	8	delete_nivel
32	Can view nivel	8	view_nivel
33	Can add tipo	9	add_tipo
34	Can change tipo	9	change_tipo
35	Can delete tipo	9	delete_tipo
36	Can view tipo	9	view_tipo
37	Can add sub materia	10	add_submateria
38	Can change sub materia	10	change_submateria
39	Can delete sub materia	10	delete_submateria
40	Can view sub materia	10	view_submateria
41	Can add questao	11	add_questao
42	Can change questao	11	change_questao
43	Can delete questao	11	delete_questao
44	Can view questao	11	view_questao
45	Can add prova respondida	12	add_provarespondida
46	Can change prova respondida	12	change_provarespondida
47	Can delete prova respondida	12	delete_provarespondida
48	Can view prova respondida	12	view_provarespondida
49	Can add prova completa	13	add_provacompleta
50	Can change prova completa	13	change_provacompleta
51	Can delete prova completa	13	delete_provacompleta
52	Can view prova completa	13	view_provacompleta
53	Can add account	14	add_account
54	Can change account	14	change_account
55	Can delete account	14	delete_account
56	Can view account	14	view_account
57	Can add media geral	15	add_mediageral
58	Can change media geral	15	change_mediageral
59	Can delete media geral	15	delete_mediageral
60	Can view media geral	15	view_mediageral
61	Can add questao respondida	16	add_questaorespondida
62	Can change questao respondida	16	change_questaorespondida
63	Can delete questao respondida	16	delete_questaorespondida
64	Can view questao respondida	16	view_questaorespondida
65	Can add simulado	17	add_simulado
66	Can change simulado	17	change_simulado
67	Can delete simulado	17	delete_simulado
68	Can view simulado	17	view_simulado
69	Can add notas	18	add_notas
70	Can change notas	18	change_notas
71	Can delete notas	18	delete_notas
72	Can view notas	18	view_notas
73	Can add aluno	19	add_aluno
74	Can change aluno	19	change_aluno
75	Can delete aluno	19	delete_aluno
76	Can view aluno	19	view_aluno
77	Can add turma	20	add_turma
78	Can change turma	20	change_turma
79	Can delete turma	20	delete_turma
80	Can view turma	20	view_turma
81	Can add professor	21	add_professor
82	Can change professor	21	change_professor
83	Can delete professor	21	delete_professor
84	Can view professor	21	view_professor
85	Can add opcao imagem	22	add_opcaoimagem
86	Can change opcao imagem	22	change_opcaoimagem
87	Can delete opcao imagem	22	delete_opcaoimagem
88	Can view opcao imagem	22	view_opcaoimagem
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: usuarios_account; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.usuarios_account (id, password, last_login, email, nome, cpf, telefone, data_nascimento, data_criacao, is_admin, is_active, is_staff, is_superuser, is_aluno, is_professor, is_verified, is_newsletter) FROM stdin;
4	pbkdf2_sha256$600000$IawhFIdu4vJceSTfQuP8nK$dQFw9Z43cha0bdZ0BN3zgN0J2/zyprRiQxyNVb/vckU=	2023-08-27 23:05:38.372304-03	teste2@gmail.com	teste	123.123.444.-44	31984603322	2000-02-01	2023-08-27 23:05:37.810655-03	f	t	f	f	t	f	f	t
1	pbkdf2_sha256$600000$V5PTQlMENoGvflZMcUQA6p$fvoqSFJ2dJwpBjIqLMB21MVgXdaFOQ8II54dAb88Tb8=	2023-09-06 19:42:23.510586-03	romfernandino@gmail.com	Roberto	701.136.996-11	31984603356	2005-03-20	2023-08-22 20:24:33.966145-03	t	t	t	t	f	f	f	t
2	pbkdf2_sha256$600000$AhN8EYmMqQqwsFRt8fC6Cj$q2fPX0FsGcGlBzgqtVENxg3jHnhXyICZnnMg0LFhNiQ=	2023-08-26 19:01:43.626235-03	diegocheib@gmail.com	cheibinho	54141133604	31984723836	2023-08-21	2023-08-26 19:01:43.040605-03	f	t	f	f	t	f	f	t
3	pbkdf2_sha256$600000$ASfRZ5vmsW9H1nmrcweZkK$9ElnY13z4NtxkhoT3gInczJz1NUxbABb1XtAlSyluak=	2023-08-27 23:00:21.554938-03	emailteste@gmail.com	robertin	123.412.313.-21	31984603343	2005-01-17	2023-08-27 23:00:21.019927-03	f	t	f	f	t	f	f	t
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2023-08-22 20:24:59.662444-03	1	Fácil	1	[{"added": {}}]	8	1
2	2023-08-22 20:25:09.572386-03	2	Média	1	[{"added": {}}]	8	1
3	2023-08-22 20:25:19.881964-03	3	Difícil	1	[{"added": {}}]	8	1
4	2023-08-22 22:08:40.746576-03	1	Fácil	1	[{"added": {}}]	8	1
5	2023-08-22 22:08:50.007484-03	2	Média	1	[{"added": {}}]	8	1
6	2023-08-22 22:08:56.896405-03	3	Dificil	1	[{"added": {}}]	8	1
7	2023-08-22 22:09:17.750543-03	1	Matematica	1	[{"added": {}}]	7	1
8	2023-08-22 22:09:55.145362-03	2	Educação Física	1	[{"added": {}}]	7	1
9	2023-08-22 22:10:00.560974-03	3	Português	1	[{"added": {}}]	7	1
10	2023-08-22 22:10:06.701538-03	4	História	1	[{"added": {}}]	7	1
11	2023-08-22 22:10:12.90525-03	5	Geografia	1	[{"added": {}}]	7	1
12	2023-08-22 22:10:28.172867-03	6	Física	1	[{"added": {}}]	7	1
13	2023-08-22 22:12:41.671272-03	7	Sociologia	1	[{"added": {}}]	7	1
14	2023-08-22 22:12:50.327375-03	8	Filosofia	1	[{"added": {}}]	7	1
15	2023-08-22 22:12:58.641956-03	9	Biologia	1	[{"added": {}}]	7	1
16	2023-08-22 22:13:06.164634-03	10	Química	1	[{"added": {}}]	7	1
17	2023-08-22 22:14:07.586967-03	11	Inglês	1	[{"added": {}}]	7	1
18	2023-08-22 22:14:12.708553-03	12	Literatura	1	[{"added": {}}]	7	1
19	2023-08-22 22:14:35.747083-03	13	Artes	1	[{"added": {}}]	7	1
20	2023-08-23 16:34:16.388827-03	16	None	3		11	1
21	2023-08-23 16:34:16.394602-03	15	None	3		11	1
22	2023-08-23 16:34:16.401345-03	14	None	3		11	1
23	2023-08-23 16:34:16.405091-03	13	None	3		11	1
24	2023-08-23 16:34:16.408036-03	12	None	3		11	1
25	2023-08-23 16:34:16.412329-03	11	None	3		11	1
26	2023-08-23 16:34:16.416784-03	10	None	3		11	1
27	2023-08-23 16:34:16.419439-03	9	None	3		11	1
28	2023-08-23 16:34:16.422035-03	8	None	3		11	1
29	2023-08-23 16:34:16.424787-03	7	None	3		11	1
30	2023-08-23 16:57:40.951534-03	26	None	3		11	1
31	2023-08-23 16:57:40.955898-03	25	None	3		11	1
32	2023-08-23 16:57:40.95907-03	24	None	3		11	1
33	2023-08-23 16:57:40.964596-03	23	None	3		11	1
34	2023-08-23 16:57:40.968371-03	22	None	3		11	1
35	2023-08-23 16:57:40.971607-03	21	None	3		11	1
36	2023-08-23 16:57:40.975094-03	20	None	3		11	1
37	2023-08-23 16:57:40.980231-03	19	None	3		11	1
38	2023-08-23 16:57:40.984514-03	18	None	3		11	1
39	2023-08-23 16:57:40.987539-03	17	None	3		11	1
40	2023-08-23 17:10:56.659976-03	1	Geometria Plana - Matematica	1	[{"added": {}}]	10	1
41	2023-08-23 17:12:00.49197-03	2	Eletrodinâmica - Física	1	[{"added": {}}]	10	1
42	2023-08-23 17:13:12.562427-03	36	None	3		11	1
43	2023-08-23 17:13:12.570109-03	35	None	3		11	1
44	2023-08-23 17:13:12.578389-03	34	None	3		11	1
45	2023-08-23 17:13:12.582561-03	33	None	3		11	1
46	2023-08-23 17:13:12.586095-03	32	None	3		11	1
47	2023-08-23 17:13:12.589911-03	31	None	3		11	1
48	2023-08-23 17:13:12.594958-03	30	None	3		11	1
49	2023-08-23 17:13:12.603531-03	29	None	3		11	1
50	2023-08-23 17:13:12.610297-03	28	None	3		11	1
51	2023-08-23 17:13:12.615781-03	27	None	3		11	1
52	2023-08-23 17:16:50.537985-03	4	None	3		11	1
53	2023-08-23 17:16:50.542361-03	3	None	3		11	1
54	2023-08-23 17:16:50.545758-03	2	None	3		11	1
55	2023-08-23 17:16:50.550632-03	1	None	3		11	1
56	2023-08-23 17:39:27.662722-03	10	None	3		11	1
57	2023-08-23 17:39:27.675124-03	9	None	3		11	1
58	2023-08-23 17:39:27.681679-03	8	None	3		11	1
59	2023-08-23 17:39:27.68715-03	7	None	3		11	1
60	2023-08-23 17:39:27.691784-03	6	None	3		11	1
61	2023-08-23 17:39:27.700324-03	5	None	3		11	1
62	2023-08-23 17:39:27.705887-03	4	None	3		11	1
63	2023-08-23 17:39:27.709855-03	3	None	3		11	1
64	2023-08-23 17:39:27.713737-03	2	None	3		11	1
65	2023-08-23 17:39:27.720308-03	1	None	3		11	1
66	2023-08-23 17:40:27.113096-03	20	None	3		11	1
67	2023-08-23 17:40:27.122216-03	19	None	3		11	1
68	2023-08-23 17:40:27.126882-03	18	None	3		11	1
69	2023-08-23 17:40:27.130617-03	17	None	3		11	1
70	2023-08-23 17:40:27.135312-03	16	None	3		11	1
71	2023-08-23 17:40:27.144358-03	15	None	3		11	1
72	2023-08-23 17:40:27.152139-03	14	None	3		11	1
73	2023-08-23 17:40:27.159426-03	13	None	3		11	1
74	2023-08-23 17:40:27.165795-03	12	None	3		11	1
75	2023-08-23 17:40:27.172027-03	11	None	3		11	1
76	2023-08-23 17:46:36.61484-03	1	None	3		11	1
77	2023-08-23 17:46:36.628462-03	2	None	3		11	1
78	2023-08-23 17:46:36.631493-03	3	None	3		11	1
79	2023-08-23 17:46:36.640092-03	4	None	3		11	1
80	2023-08-23 17:46:36.649447-03	5	None	3		11	1
81	2023-08-23 17:46:36.659507-03	6	None	3		11	1
82	2023-08-23 17:46:36.665607-03	7	None	3		11	1
83	2023-08-23 17:46:36.673906-03	8	None	3		11	1
84	2023-08-23 17:46:36.682453-03	9	None	3		11	1
85	2023-08-23 17:46:36.693056-03	10	None	3		11	1
86	2023-08-23 17:48:31.078189-03	1	None	2	[{"changed": {"fields": ["Enunciado", "Nivel"]}}]	11	1
87	2023-08-23 17:49:48.805729-03	1	None	3		11	1
88	2023-08-23 17:49:48.83371-03	2	None	3		11	1
89	2023-08-23 17:49:48.837961-03	3	None	3		11	1
90	2023-08-23 17:49:48.842066-03	4	None	3		11	1
91	2023-08-23 17:49:48.847459-03	5	None	3		11	1
92	2023-08-23 17:49:48.855354-03	6	None	3		11	1
93	2023-08-23 17:49:48.861939-03	7	None	3		11	1
94	2023-08-23 17:49:48.866041-03	8	None	3		11	1
95	2023-08-23 17:49:48.869088-03	9	None	3		11	1
96	2023-08-23 17:49:48.873892-03	10	None	3		11	1
97	2023-08-23 17:50:50.732753-03	1	None	2	[{"changed": {"fields": ["Enunciado", "Nivel"]}}]	11	1
98	2023-08-23 17:51:05.961513-03	2	Medio	2	[{"changed": {"fields": ["Nivel"]}}]	8	1
99	2023-08-23 17:51:10.535039-03	1	None	2	[]	11	1
100	2023-08-23 17:51:34.569297-03	1	None	3		11	1
101	2023-08-23 17:51:34.573821-03	2	None	3		11	1
102	2023-08-23 17:51:34.58271-03	3	None	3		11	1
103	2023-08-23 17:51:34.591319-03	4	None	3		11	1
104	2023-08-23 17:51:34.597299-03	5	None	3		11	1
105	2023-08-23 17:51:34.601895-03	6	None	3		11	1
106	2023-08-23 17:51:34.60592-03	7	None	3		11	1
107	2023-08-23 17:51:34.609863-03	8	None	3		11	1
108	2023-08-23 17:51:34.615714-03	9	None	3		11	1
109	2023-08-23 17:51:34.62183-03	10	None	3		11	1
110	2023-08-23 17:52:55.128117-03	1	None	2	[{"changed": {"fields": ["Enunciado", "Nivel", "Tipo"]}}]	11	1
111	2023-08-23 17:59:33.468329-03	1	Lei de Ohm - Eletrodinâmica - Física	1	[{"added": {}}]	6	1
112	2023-08-23 20:56:12.647478-03	3	Geometria Analitica - Matematica	1	[{"added": {}}]	10	1
113	2023-08-23 20:56:37.43146-03	2	Cordenadas - Geometria Analitica - Matematica	1	[{"added": {}}]	6	1
114	2023-08-23 20:56:50.495997-03	3	Circunferencia - Geometria Plana - Matematica	1	[{"added": {}}]	6	1
115	2023-08-24 16:04:40.189571-03	1	None	3		11	1
116	2023-08-24 16:04:40.200586-03	2	None	3		11	1
117	2023-08-24 16:04:40.204937-03	3	None	3		11	1
118	2023-08-24 16:04:40.207901-03	4	None	3		11	1
119	2023-08-24 16:04:40.211127-03	5	None	3		11	1
120	2023-08-24 16:04:40.214-03	6	None	3		11	1
121	2023-08-24 16:04:40.21804-03	7	None	3		11	1
122	2023-08-24 16:04:40.220757-03	8	None	3		11	1
123	2023-08-24 16:04:40.223384-03	9	None	3		11	1
124	2023-08-24 16:04:40.226002-03	10	None	3		11	1
125	2023-08-24 16:13:36.855967-03	11	None	3		11	1
126	2023-08-24 16:13:36.862456-03	12	None	3		11	1
127	2023-08-24 16:13:36.865818-03	13	None	3		11	1
128	2023-08-24 16:15:02.643484-03	4	Geometria - Matematica	1	[{"added": {}}]	10	1
129	2023-08-24 16:15:32.731914-03	4	Geometria - Matematica	3		10	1
130	2023-08-24 16:35:41.541465-03	1	Matemática	2	[{"changed": {"fields": ["Nome"]}}]	7	1
131	2023-08-24 16:53:48.184028-03	2	Médio	2	[{"changed": {"fields": ["Nivel"]}}]	8	1
132	2023-08-24 17:44:27.451643-03	1	None	3		11	1
133	2023-08-24 17:44:27.458533-03	2	None	3		11	1
134	2023-08-24 17:44:27.462722-03	3	None	3		11	1
135	2023-08-24 17:44:27.46812-03	4	None	3		11	1
136	2023-08-24 17:44:27.474864-03	5	None	3		11	1
137	2023-08-24 17:44:27.48137-03	6	None	3		11	1
138	2023-08-24 17:44:27.48636-03	7	None	3		11	1
139	2023-08-24 17:44:27.490747-03	8	None	3		11	1
140	2023-08-24 17:44:27.495038-03	9	None	3		11	1
141	2023-08-24 17:44:27.501656-03	10	None	3		11	1
142	2023-08-24 18:03:14.89911-03	1	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
143	2023-08-24 18:03:14.904358-03	2	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
144	2023-08-24 18:03:14.908665-03	3	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
145	2023-08-24 18:03:14.914884-03	4	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
146	2023-08-24 18:03:14.920206-03	5	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
147	2023-08-24 18:03:14.92439-03	6	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
148	2023-08-24 18:03:14.928026-03	7	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
149	2023-08-24 18:03:14.931827-03	8	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
150	2023-08-24 18:43:59.907859-03	9	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
151	2023-08-24 18:43:59.91785-03	10	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
152	2023-08-24 19:13:14.849871-03	1	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
153	2023-08-24 19:13:14.856047-03	2	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
154	2023-08-24 19:13:14.859844-03	3	Análise de Tempo - Tempo - Matemática	3		11	1
155	2023-08-24 19:13:14.862729-03	4	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
156	2023-08-24 19:13:14.868832-03	5	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
157	2023-08-24 19:13:14.871992-03	6	Análise de Tempo - Tempo - Matemática	3		11	1
158	2023-08-24 19:13:14.87477-03	7	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
159	2023-08-24 19:13:14.879264-03	8	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
160	2023-08-24 19:13:14.884885-03	9	Análise de Tempo - Tempo - Matemática	3		11	1
161	2023-08-24 19:13:14.887674-03	10	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
162	2023-08-24 19:13:14.890348-03	11	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
163	2023-08-24 19:13:14.89295-03	12	Análise de Tempo - Tempo - Matemática	3		11	1
164	2023-08-24 19:13:14.898515-03	13	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
165	2023-08-24 19:13:14.901583-03	14	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
166	2023-08-24 19:13:14.904176-03	15	Análise de Tempo - Tempo - Matemática	3		11	1
167	2023-08-24 19:17:09.381468-03	3	Análise de Tempo - Tempo - Matemática	3		11	1
168	2023-08-24 19:17:38.475895-03	1	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
169	2023-08-24 19:17:38.480532-03	2	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
170	2023-08-24 19:17:38.483964-03	4	Análise de Tempo - Unidades de medida - Matemática	3		11	1
171	2023-08-24 19:17:38.488922-03	5	Propagacao de Energia - Eletricidade - Física	3		11	1
172	2023-08-24 19:18:44.285097-03	3	Difícil	2	[{"changed": {"fields": ["Nivel"]}}]	8	1
173	2023-08-24 19:20:20.38749-03	1	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
174	2023-08-24 19:20:20.39271-03	2	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
175	2023-08-24 19:20:20.3953-03	3	Análise de Tempo - Unidades de medida - Matemática	3		11	1
176	2023-08-24 19:20:20.398076-03	4	Análise de Tempo - Unidades de medida - Matemática	3		11	1
177	2023-08-24 19:20:20.400714-03	5	Propagacao de Energia - Eletricidade - Física	3		11	1
178	2023-08-24 19:20:20.403653-03	6	Variacao de Posicao - Movimento - Matemática	3		11	1
179	2023-08-24 19:20:20.407036-03	7	Velocidade Média - Movimento - Matemática	3		11	1
180	2023-08-24 19:20:20.409905-03	8	Propagação de Energia - Eletricidade - Física	3		11	1
181	2023-08-24 19:20:20.412795-03	9	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
182	2023-08-24 19:20:20.415537-03	10	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
183	2023-08-24 19:20:20.418055-03	11	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
184	2023-08-24 19:20:20.423545-03	12	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
185	2023-08-24 19:20:20.427815-03	13	Análise de Tempo - Unidades de medida - Matemática	3		11	1
186	2023-08-24 19:20:20.430298-03	14	Análise de Tempo - Unidades de medida - Matemática	3		11	1
187	2023-08-24 19:20:20.432924-03	15	Propagacao de Energia - Eletricidade - Física	3		11	1
188	2023-08-24 19:20:20.435813-03	16	Variacao de Posicao - Movimento - Matemática	3		11	1
327	2023-08-25 00:47:43.929438-03	54	Lei de Hubble - Hubble - Física	3		11	1
189	2023-08-24 19:20:20.438658-03	17	Velocidade Média - Movimento - Matemática	3		11	1
190	2023-08-24 19:20:20.443458-03	18	Propagação de Energia - Eletricidade - Física	3		11	1
191	2023-08-24 19:20:20.446503-03	19	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
192	2023-08-24 19:20:20.451076-03	20	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
193	2023-08-24 19:57:40.698124-03	21	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
194	2023-08-24 19:57:40.706889-03	22	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
195	2023-08-24 19:57:40.711686-03	23	Análise de Tempo - Unidades de medida - Matemática	3		11	1
196	2023-08-24 19:57:40.715272-03	24	Análise de Tempo - Unidades de medida - Matemática	3		11	1
197	2023-08-24 19:57:40.720268-03	25	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
198	2023-08-24 19:57:40.72597-03	26	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
199	2023-08-24 19:57:40.729046-03	27	Análise de Tempo - Unidades de medida - Matemática	3		11	1
200	2023-08-24 19:57:40.732441-03	28	Análise de Tempo - Unidades de medida - Matemática	3		11	1
201	2023-08-24 19:57:40.736338-03	29	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
202	2023-08-24 19:57:40.740202-03	30	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
203	2023-08-24 19:57:40.743542-03	31	Análise de Tempo - Unidades de medida - Matemática	3		11	1
204	2023-08-24 19:57:40.748703-03	32	Análise de Tempo - Unidades de medida - Matemática	3		11	1
205	2023-08-24 19:57:40.755554-03	33	Movimento em Duas Dimensões - Forças e Aceleração - Física	3		11	1
206	2023-08-24 19:57:40.758465-03	34	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
207	2023-08-24 19:57:40.761421-03	35	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
208	2023-08-24 19:57:40.76552-03	36	Análise de Tempo - Unidades de medida - Matemática	3		11	1
209	2023-08-24 19:57:40.769544-03	37	Análise de Tempo - Unidades de medida - Matemática	3		11	1
210	2023-08-24 19:57:40.777403-03	38	Movimento em Duas Dimensões - Forças e Aceleração - Física	3		11	1
211	2023-08-24 19:58:04.411216-03	39	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
212	2023-08-24 19:58:04.420318-03	40	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
213	2023-08-24 19:58:04.429305-03	41	Análise de Tempo - Unidades de medida - Matemática	3		11	1
214	2023-08-24 19:58:04.434426-03	42	Análise de Tempo - Unidades de medida - Matemática	3		11	1
215	2023-08-24 19:58:04.438491-03	43	Movimento em Duas Dimensões - Forças e Aceleração - Física	3		11	1
216	2023-08-24 19:58:04.44223-03	44	Lei de Newtown - Impacto e Colisões - Física	3		11	1
217	2023-08-24 19:58:04.445174-03	45	Propagacao de Energia - Eletricidade - Física	3		11	1
218	2023-08-24 19:58:04.450342-03	46	Variacao de Posicao - Movimento - Matemática	3		11	1
219	2023-08-24 19:58:04.455927-03	47	Velocidade Média - Movimento - Matemática	3		11	1
220	2023-08-24 19:58:04.459381-03	48	Propagação de Energia - Eletricidade - Física	3		11	1
221	2023-08-24 19:58:04.462192-03	49	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
222	2023-08-24 19:58:04.46507-03	50	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
223	2023-08-24 19:58:04.468818-03	51	Lei de Hubble - Hubble - Física	3		11	1
224	2023-08-24 19:58:04.47213-03	52	Leitura de Musica - Interpretação de texto - Português	3		11	1
225	2023-08-24 19:58:04.476378-03	53	Lei de Newtown - Impacto e Colisões - Física	3		11	1
226	2023-08-24 21:21:07.6354-03	1	MediaGeral object (1)	1	[{"added": {}}]	15	1
227	2023-08-24 21:21:19.932733-03	2	MediaGeral object (2)	1	[{"added": {}}]	15	1
228	2023-08-24 21:21:36.300972-03	3	MediaGeral object (3)	1	[{"added": {}}]	15	1
229	2023-08-24 23:49:18.816394-03	3	MediaGeral object (3)	2	[]	15	1
230	2023-08-25 00:38:46.703492-03	1	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
231	2023-08-25 00:38:46.71389-03	2	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
232	2023-08-25 00:38:46.720519-03	3	Análise de Tempo - Unidades de medida - Matemática	3		11	1
233	2023-08-25 00:38:46.727955-03	4	Análise de Tempo - Unidades de medida - Matemática	3		11	1
234	2023-08-25 00:38:46.732978-03	5	Movimento em Duas Dimensões - Forças e Aceleração - Física	3		11	1
235	2023-08-25 00:38:46.737478-03	6	Lei de Newtown - Impacto e Colisões - Física	3		11	1
236	2023-08-25 00:38:46.741634-03	7	Propagacao de Energia - Eletricidade - Física	3		11	1
237	2023-08-25 00:38:46.750914-03	8	Variacao de Posicao - Movimento - Matemática	3		11	1
238	2023-08-25 00:38:46.758641-03	9	Velocidade Média - Movimento - Matemática	3		11	1
239	2023-08-25 00:38:46.762637-03	10	Propagação de Energia - Eletricidade - Física	3		11	1
240	2023-08-25 00:38:46.767123-03	11	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
241	2023-08-25 00:38:46.770849-03	12	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
242	2023-08-25 00:38:46.774571-03	13	Lei de Hubble - Hubble - Física	3		11	1
243	2023-08-25 00:38:46.780892-03	14	Leitura de Musica - Interpretação de texto - Português	3		11	1
244	2023-08-25 00:38:46.788177-03	15	Lei de Newtown - Impacto e Colisões - Física	3		11	1
245	2023-08-25 00:40:25.473394-03	1	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
246	2023-08-25 00:40:25.483639-03	2	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
247	2023-08-25 00:40:25.492324-03	3	Análise de Tempo - Unidades de medida - Matemática	3		11	1
248	2023-08-25 00:40:25.49588-03	4	Análise de Tempo - Unidades de medida - Matemática	3		11	1
249	2023-08-25 00:40:25.499677-03	5	Movimento em Duas Dimensões - Forças e Aceleração - Física	3		11	1
250	2023-08-25 00:40:25.504599-03	6	Lei de Newtown - Impacto e Colisões - Física	3		11	1
251	2023-08-25 00:40:25.508228-03	7	Propagacao de Energia - Eletricidade - Física	3		11	1
252	2023-08-25 00:40:25.513492-03	8	Variacao de Posicao - Movimento - Matemática	3		11	1
253	2023-08-25 00:40:25.520597-03	9	Velocidade Média - Movimento - Matemática	3		11	1
254	2023-08-25 00:40:25.529153-03	10	Propagação de Energia - Eletricidade - Física	3		11	1
255	2023-08-25 00:40:25.533949-03	11	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
256	2023-08-25 00:40:25.537681-03	12	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
257	2023-08-25 00:40:25.540788-03	13	Lei de Hubble - Hubble - Física	3		11	1
258	2023-08-25 00:40:25.545534-03	14	Leitura de Musica - Interpretação de texto - Português	3		11	1
259	2023-08-25 00:40:25.553294-03	15	Lei de Newtown - Impacto e Colisões - Física	3		11	1
260	2023-08-25 00:41:19.59365-03	1	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
261	2023-08-25 00:41:19.599122-03	2	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
262	2023-08-25 00:41:19.604961-03	3	Análise de Tempo - Unidades de medida - Matemática	3		11	1
263	2023-08-25 00:41:19.609313-03	4	Análise de Tempo - Unidades de medida - Matemática	3		11	1
264	2023-08-25 00:41:19.613479-03	5	Lei de Newtown - Impacto e Colisões - Física	3		11	1
265	2023-08-25 00:41:19.619818-03	6	Propagacao de Energia - Eletricidade - Física	3		11	1
266	2023-08-25 00:41:19.629618-03	7	Variacao de Posicao - Movimento - Matemática	3		11	1
267	2023-08-25 00:41:19.63384-03	8	Velocidade Média - Movimento - Matemática	3		11	1
268	2023-08-25 00:41:19.637628-03	9	Propagação de Energia - Eletricidade - Física	3		11	1
269	2023-08-25 00:41:19.644047-03	10	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
270	2023-08-25 00:41:19.652106-03	11	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
271	2023-08-25 00:41:19.657835-03	12	Lei de Hubble - Hubble - Física	3		11	1
272	2023-08-25 00:41:19.663421-03	13	Leitura de Musica - Interpretação de texto - Português	3		11	1
273	2023-08-25 00:41:19.668964-03	14	Lei de Newtown - Impacto e Colisões - Física	3		11	1
274	2023-08-25 00:43:04.424544-03	1	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
275	2023-08-25 00:43:04.430373-03	2	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
276	2023-08-25 00:43:04.434162-03	3	Análise de Tempo - Unidades de medida - Matemática	3		11	1
277	2023-08-25 00:43:04.438084-03	4	Análise de Tempo - Unidades de medida - Matemática	3		11	1
278	2023-08-25 00:43:04.441397-03	5	Lei de Newtown - Impacto e Colisões - Física	3		11	1
279	2023-08-25 00:43:04.446663-03	6	Propagacao de Energia - Eletricidade - Física	3		11	1
280	2023-08-25 00:43:04.454314-03	7	Variacao de Posicao - Movimento - Matemática	3		11	1
281	2023-08-25 00:43:04.457807-03	8	Velocidade Média - Movimento - Matemática	3		11	1
282	2023-08-25 00:43:04.461907-03	9	Propagação de Energia - Eletricidade - Física	3		11	1
283	2023-08-25 00:43:04.465306-03	10	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
284	2023-08-25 00:43:04.469757-03	11	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
285	2023-08-25 00:43:04.476127-03	12	Lei de Hubble - Hubble - Física	3		11	1
286	2023-08-25 00:43:04.482688-03	13	Leitura de Musica - Interpretação de texto - Português	3		11	1
287	2023-08-25 00:43:04.485789-03	14	Lei de Newtown - Impacto e Colisões - Física	3		11	1
288	2023-08-25 00:47:43.776101-03	15	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
289	2023-08-25 00:47:43.783591-03	16	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
290	2023-08-25 00:47:43.791345-03	17	Análise de Tempo - Unidades de medida - Matemática	3		11	1
291	2023-08-25 00:47:43.794905-03	18	Análise de Tempo - Unidades de medida - Matemática	3		11	1
292	2023-08-25 00:47:43.798445-03	19	Lei de Newtown - Impacto e Colisões - Física	3		11	1
293	2023-08-25 00:47:43.801805-03	20	Propagacao de Energia - Eletricidade - Física	3		11	1
294	2023-08-25 00:47:43.806816-03	21	Variacao de Posicao - Movimento - Matemática	3		11	1
295	2023-08-25 00:47:43.813329-03	22	Velocidade Média - Movimento - Matemática	3		11	1
296	2023-08-25 00:47:43.817695-03	23	Propagação de Energia - Eletricidade - Física	3		11	1
297	2023-08-25 00:47:43.82164-03	24	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
298	2023-08-25 00:47:43.824327-03	25	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
299	2023-08-25 00:47:43.827006-03	26	Lei de Hubble - Hubble - Física	3		11	1
300	2023-08-25 00:47:43.830972-03	27	Leitura de Musica - Interpretação de texto - Português	3		11	1
301	2023-08-25 00:47:43.834324-03	28	Lei de Newtown - Impacto e Colisões - Física	3		11	1
302	2023-08-25 00:47:43.838528-03	29	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
303	2023-08-25 00:47:43.844247-03	30	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
304	2023-08-25 00:47:43.847348-03	31	Análise de Tempo - Unidades de medida - Matemática	3		11	1
305	2023-08-25 00:47:43.851254-03	32	Análise de Tempo - Unidades de medida - Matemática	3		11	1
306	2023-08-25 00:47:43.854603-03	33	Lei de Newtown - Impacto e Colisões - Física	3		11	1
307	2023-08-25 00:47:43.85719-03	34	Propagacao de Energia - Eletricidade - Física	3		11	1
308	2023-08-25 00:47:43.859734-03	35	Variacao de Posicao - Movimento - Matemática	3		11	1
309	2023-08-25 00:47:43.863318-03	36	Velocidade Média - Movimento - Matemática	3		11	1
310	2023-08-25 00:47:43.867226-03	37	Propagação de Energia - Eletricidade - Física	3		11	1
311	2023-08-25 00:47:43.870475-03	38	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
312	2023-08-25 00:47:43.87443-03	39	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
313	2023-08-25 00:47:43.880078-03	40	Lei de Hubble - Hubble - Física	3		11	1
314	2023-08-25 00:47:43.882907-03	41	Leitura de Musica - Interpretação de texto - Português	3		11	1
315	2023-08-25 00:47:43.886654-03	42	Lei de Newtown - Impacto e Colisões - Física	3		11	1
316	2023-08-25 00:47:43.890543-03	43	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
317	2023-08-25 00:47:43.893293-03	44	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
318	2023-08-25 00:47:43.896654-03	45	Análise de Tempo - Unidades de medida - Matemática	3		11	1
319	2023-08-25 00:47:43.900247-03	46	Análise de Tempo - Unidades de medida - Matemática	3		11	1
320	2023-08-25 00:47:43.903378-03	47	Lei de Newtown - Impacto e Colisões - Física	3		11	1
321	2023-08-25 00:47:43.906886-03	48	Propagacao de Energia - Eletricidade - Física	3		11	1
322	2023-08-25 00:47:43.912877-03	49	Variacao de Posicao - Movimento - Matemática	3		11	1
323	2023-08-25 00:47:43.916999-03	50	Velocidade Média - Movimento - Matemática	3		11	1
324	2023-08-25 00:47:43.920352-03	51	Propagação de Energia - Eletricidade - Física	3		11	1
325	2023-08-25 00:47:43.923933-03	52	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
326	2023-08-25 00:47:43.926565-03	53	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
328	2023-08-25 00:47:43.933029-03	55	Leitura de Musica - Interpretação de texto - Português	3		11	1
329	2023-08-25 00:47:43.936711-03	56	Lei de Newtown - Impacto e Colisões - Física	3		11	1
330	2023-08-25 00:47:43.939614-03	57	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
331	2023-08-25 00:47:43.942382-03	58	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
332	2023-08-25 00:47:43.945301-03	59	Análise de Tempo - Unidades de medida - Matemática	3		11	1
333	2023-08-25 00:47:43.948939-03	60	Análise de Tempo - Unidades de medida - Matemática	3		11	1
334	2023-08-25 00:47:43.954926-03	61	Lei de Newtown - Impacto e Colisões - Física	3		11	1
335	2023-08-25 00:47:43.957763-03	62	Propagacao de Energia - Eletricidade - Física	3		11	1
336	2023-08-25 00:47:43.961014-03	63	Variacao de Posicao - Movimento - Matemática	3		11	1
337	2023-08-25 00:47:43.965466-03	64	Velocidade Média - Movimento - Matemática	3		11	1
338	2023-08-25 00:47:43.96835-03	65	Propagação de Energia - Eletricidade - Física	3		11	1
339	2023-08-25 00:47:43.972564-03	66	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
340	2023-08-25 00:47:43.978294-03	67	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
341	2023-08-25 00:47:43.98125-03	68	Lei de Hubble - Hubble - Física	3		11	1
342	2023-08-25 00:47:43.983897-03	69	Leitura de Musica - Interpretação de texto - Português	3		11	1
343	2023-08-25 00:47:43.988287-03	70	Lei de Newtown - Impacto e Colisões - Física	3		11	1
344	2023-08-25 00:47:43.991292-03	71	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
345	2023-08-25 00:47:43.994638-03	72	Matemática Básica - Analise de Gráfico - Matemática	3		11	1
346	2023-08-25 00:47:43.99864-03	73	Análise de Tempo - Unidades de medida - Matemática	3		11	1
347	2023-08-25 00:47:44.001811-03	74	Análise de Tempo - Unidades de medida - Matemática	3		11	1
348	2023-08-25 00:47:44.006293-03	75	Lei de Newtown - Impacto e Colisões - Física	3		11	1
349	2023-08-25 00:47:44.012057-03	76	Propagacao de Energia - Eletricidade - Física	3		11	1
350	2023-08-25 00:47:44.015215-03	77	Variacao de Posicao - Movimento - Matemática	3		11	1
351	2023-08-25 00:47:44.017846-03	78	Velocidade Média - Movimento - Matemática	3		11	1
352	2023-08-25 00:47:44.021488-03	79	Propagação de Energia - Eletricidade - Física	3		11	1
353	2023-08-25 00:47:44.02479-03	80	Média e Interpretação de Dados - Análise de Dados - Matemática	3		11	1
354	2023-08-25 00:47:44.027661-03	81	Cálculos de Tempo e Distância - Tempo - Matemática	3		11	1
355	2023-08-25 00:47:44.030795-03	82	Lei de Hubble - Hubble - Física	3		11	1
356	2023-08-25 00:47:44.033948-03	83	Leitura de Musica - Interpretação de texto - Português	3		11	1
357	2023-08-25 00:47:44.03746-03	84	Lei de Newtown - Impacto e Colisões - Física	3		11	1
358	2023-08-25 00:49:12.988185-03	6	Propagacao de Energia - Eletricidade - Física	2	[{"changed": {"fields": ["Enunciado", "Imagem"]}}]	11	1
359	2023-08-25 00:49:22.974007-03	7	Variacao de Posicao - Movimento - Matemática	2	[{"changed": {"fields": ["Enunciado", "Imagem"]}}]	11	1
360	2023-08-25 00:49:28.009706-03	8	Velocidade Média - Movimento - Matemática	2	[{"changed": {"fields": ["Enunciado", "Imagem"]}}]	11	1
361	2023-08-25 00:49:37.381677-03	9	Propagação de Energia - Eletricidade - Física	2	[{"changed": {"fields": ["Enunciado", "Imagem"]}}]	11	1
362	2023-08-25 00:49:44.876979-03	10	Média e Interpretação de Dados - Análise de Dados - Matemática	2	[{"changed": {"fields": ["Enunciado", "Imagem"]}}]	11	1
363	2023-08-25 16:43:35.329012-03	1	Matemática Básica - Analise de Gráfico - Matemática	2	[{"changed": {"fields": ["Enunciado"]}}]	11	1
364	2023-08-27 09:56:48.612141-03	1	materiais.Conteudo.None	2	[{"changed": {"fields": ["Conteudo"]}}]	11	1
365	2023-08-27 10:00:33.705977-03	2	materiais.Conteudo.None	2	[{"changed": {"fields": ["Enunciado", "Conteudo"]}}]	11	1
366	2023-08-27 10:09:21.548137-03	6	materiais.Conteudo.None	2	[{"changed": {"fields": ["Conteudo"]}}]	11	1
367	2023-08-27 10:09:44.084301-03	7	Propagacao de Energia - Eletricidade - Física	3		6	1
368	2023-08-27 10:09:54.34046-03	5	Análise de Tempo - Tempo - Matemática	3		6	1
369	2023-08-27 10:10:59.479123-03	8	Variação de Posição - Movimento - Matemática	2	[{"changed": {"fields": ["Nome"]}}]	6	1
370	2023-08-27 10:11:25.625338-03	5	materiais.Conteudo.None	2	[{"changed": {"fields": ["Enunciado", "Conteudo"]}}]	11	1
371	2023-08-27 10:53:24.062678-03	17	Comprimento - Unidades de medida - Matemática	1	[{"added": {}}]	6	1
372	2023-08-27 10:54:08.492665-03	3	3 - Médio	2	[{"changed": {"fields": ["Enunciado", "Conteudo"]}}]	11	1
373	2023-08-27 10:54:40.298621-03	4	4 - Médio	2	[{"changed": {"fields": ["Enunciado", "Conteudo"]}}]	11	1
374	2023-08-27 10:54:55.079078-03	6	6 - Médio	2	[{"changed": {"fields": ["Conteudo"]}}]	11	1
375	2023-08-27 10:55:39.859397-03	7	7 - Difícil	2	[{"changed": {"fields": ["Conteudo"]}}]	11	1
376	2023-08-27 10:56:28.676573-03	8	8 - Médio	2	[{"changed": {"fields": ["Conteudo", "Tipo"]}}]	11	1
377	2023-08-27 10:56:59.704476-03	9	9 - Médio	2	[{"changed": {"fields": ["Conteudo"]}}]	11	1
378	2023-08-27 10:57:13.466862-03	10	10 - Médio	2	[{"changed": {"fields": ["Conteudo"]}}]	11	1
379	2023-08-27 10:57:29.531301-03	11	11 - Médio	2	[{"changed": {"fields": ["Enunciado", "Conteudo"]}}]	11	1
380	2023-08-27 11:01:36.982813-03	12	12 - Difícil	2	[{"changed": {"fields": ["Enunciado", "Opcoes", "Conteudo"]}}]	11	1
381	2023-08-27 11:01:50.207567-03	13	13 - Fácil	2	[{"changed": {"fields": ["Enunciado", "Conteudo"]}}]	11	1
382	2023-08-27 11:02:06.980797-03	14	14 - Difícil	2	[{"changed": {"fields": ["Enunciado", "Conteudo"]}}]	11	1
383	2023-08-27 11:03:28.339935-03	14	14 - Difícil	2	[]	11	1
384	2023-08-27 11:06:03.0392-03	5	5 - Difícil	2	[{"changed": {"fields": ["Imagem"]}}]	11	1
385	2023-08-27 11:06:10.557244-03	14	14 - Difícil	3		11	1
386	2023-08-27 11:10:01.84935-03	6	6 - Médio	2	[{"changed": {"fields": ["Enunciado", "Opcoes"]}}]	11	1
387	2023-08-27 14:32:48.350968-03	5	ProvaRespondida object (5)	3		12	1
388	2023-08-27 14:32:48.357959-03	4	ProvaRespondida object (4)	3		12	1
389	2023-08-27 14:32:48.362863-03	3	ProvaRespondida object (3)	3		12	1
390	2023-08-27 14:32:48.368695-03	2	ProvaRespondida object (2)	3		12	1
391	2023-08-27 14:32:48.371886-03	1	ProvaRespondida object (1)	3		12	1
392	2023-08-27 14:33:22.918617-03	3	matematica 2023-08-27 16:54:16.251811+00:00	3		13	1
393	2023-08-27 14:33:27.106599-03	5	natureza 2023-08-27 17:31:33.300958+00:00	3		13	1
394	2023-08-27 14:33:31.65432-03	4	matematica 2023-08-27 16:54:26.015871+00:00	3		13	1
395	2023-08-27 14:33:36.922851-03	2	matematica 2023-08-27 16:53:11.022829+00:00	3		13	1
396	2023-08-27 14:34:25.613935-03	1	ProvaCompleta object (1)	3		13	1
397	2023-08-27 14:35:19.752082-03	6	natureza 2023-08-27 17:34:51.138603+00:00	3		13	1
398	2023-08-27 15:40:51.640907-03	17	matematica 2023-08-27 18:28:13.449400+00:00	3		13	1
399	2023-08-27 15:40:57.413362-03	9	matematica 2023-08-27 17:49:51.146310+00:00	3		13	1
400	2023-08-27 15:40:57.418221-03	8	matematica 2023-08-27 17:46:56.003839+00:00	3		13	1
401	2023-08-27 15:40:57.422837-03	7	natureza 2023-08-27 17:41:02.783413+00:00	3		13	1
402	2023-08-27 15:41:01.030884-03	10	natureza - matematica 2023-08-27 18:07:47.858812+00:00	3		13	1
403	2023-08-27 15:41:04.908319-03	11	matematica 2023-08-27 18:09:08.529025+00:00	3		13	1
404	2023-08-27 15:41:23.375816-03	16	ProvaCompleta object (16)	3		13	1
405	2023-08-27 15:41:27.112871-03	15	ProvaCompleta object (15)	3		13	1
406	2023-08-27 15:41:27.122995-03	14	ProvaCompleta object (14)	3		13	1
407	2023-08-27 15:41:27.127841-03	13	ProvaCompleta object (13)	3		13	1
408	2023-08-27 15:41:27.134552-03	12	ProvaCompleta object (12)	3		13	1
409	2023-08-27 15:51:03.974657-03	18	Roberto - 2023-08-27 18:43:11.523486+00:00	3		13	1
410	2023-08-27 17:07:08.529297-03	1	Ciencias da Natureza	1	[{"added": {}}]	17	1
411	2023-08-27 17:07:18.346512-03	2	Ciencias Humanas e suas Tecnologias	1	[{"added": {}}]	17	1
412	2023-08-27 17:07:40.938163-03	1	Ciências da Natureza	2	[{"changed": {"fields": ["Tipo"]}}]	17	1
413	2023-08-27 17:07:51.527275-03	2	Ciências Humanas	2	[{"changed": {"fields": ["Tipo"]}}]	17	1
414	2023-08-27 17:07:56.14167-03	3	Matemática	1	[{"added": {}}]	17	1
415	2023-08-27 17:08:05.523715-03	4	Linguagens e suas Tecnologias	1	[{"added": {}}]	17	1
416	2023-08-27 18:00:39.838824-03	4	Linguagens e suas Tecnologias	2	[{"changed": {"fields": ["Materia"]}}]	17	1
417	2023-08-27 18:00:47.099325-03	3	Matemática	2	[{"changed": {"fields": ["Materia"]}}]	17	1
418	2023-08-27 18:01:21.07359-03	2	Ciências Humanas	2	[{"changed": {"fields": ["Materia"]}}]	17	1
419	2023-08-27 18:01:37.433618-03	1	Ciências da Natureza	2	[{"changed": {"fields": ["Materia"]}}]	17	1
420	2023-08-27 19:05:55.295714-03	4	Linguagens e suas Tecnologias	2	[]	17	1
421	2023-08-27 19:05:57.563706-03	3	Matemática	2	[]	17	1
422	2023-08-27 19:06:02.304868-03	2	Ciências Humanas	2	[]	17	1
423	2023-08-27 19:06:05.15595-03	1	Ciências da Natureza	2	[]	17	1
424	2023-08-27 21:19:32.242332-03	1	Ciências da Natureza	2	[{"changed": {"fields": ["Materia"]}}]	17	1
425	2023-08-27 22:21:27.180974-03	32	Roberto - 2023-08-28 01:20:53.702276+00:00	3		13	1
426	2023-08-27 22:21:27.184474-03	31	Roberto - 2023-08-28 01:20:53.467903+00:00	3		13	1
427	2023-08-27 22:21:27.187204-03	30	Roberto - 2023-08-28 01:19:57.005048+00:00	3		13	1
428	2023-08-27 22:21:27.190494-03	29	Roberto - 2023-08-28 01:19:56.665965+00:00	3		13	1
429	2023-08-27 22:21:27.194264-03	28	Roberto - 2023-08-28 01:19:36.340726+00:00	3		13	1
430	2023-08-27 22:21:27.198052-03	27	Roberto - 2023-08-28 01:15:43.262931+00:00	3		13	1
431	2023-08-27 22:21:27.201006-03	26	Roberto - 2023-08-28 01:03:21.059394+00:00	3		13	1
432	2023-08-27 22:21:27.203631-03	25	Roberto - 2023-08-28 01:00:40.829556+00:00	3		13	1
433	2023-08-27 22:21:27.206011-03	24	Roberto - 2023-08-28 00:58:26.027843+00:00	3		13	1
434	2023-08-27 22:21:27.210511-03	23	Roberto - 2023-08-28 00:57:23.050382+00:00	3		13	1
435	2023-08-27 22:21:27.213874-03	22	Roberto - 2023-08-28 00:55:56.169347+00:00	3		13	1
436	2023-08-27 22:21:27.216687-03	21	Roberto - 2023-08-27 19:38:21.483997+00:00	3		13	1
437	2023-08-27 22:23:51.595544-03	119	QuestaoRespondida object (119)	3		16	1
438	2023-08-27 22:23:51.602613-03	118	QuestaoRespondida object (118)	3		16	1
439	2023-08-27 22:23:51.607107-03	117	QuestaoRespondida object (117)	3		16	1
440	2023-08-27 22:23:51.612645-03	116	QuestaoRespondida object (116)	3		16	1
441	2023-08-27 22:23:51.615302-03	115	QuestaoRespondida object (115)	3		16	1
442	2023-08-27 22:23:51.617833-03	114	QuestaoRespondida object (114)	3		16	1
443	2023-08-27 22:23:51.62056-03	113	QuestaoRespondida object (113)	3		16	1
444	2023-08-27 22:23:51.623258-03	112	QuestaoRespondida object (112)	3		16	1
445	2023-08-27 22:23:51.628994-03	111	QuestaoRespondida object (111)	3		16	1
446	2023-08-27 22:23:51.633361-03	110	QuestaoRespondida object (110)	3		16	1
447	2023-08-27 22:23:51.636404-03	109	QuestaoRespondida object (109)	3		16	1
448	2023-08-27 22:23:51.639122-03	108	QuestaoRespondida object (108)	3		16	1
449	2023-08-27 22:23:51.643627-03	107	QuestaoRespondida object (107)	3		16	1
450	2023-08-27 22:23:51.648946-03	106	QuestaoRespondida object (106)	3		16	1
451	2023-08-27 22:23:51.651986-03	105	QuestaoRespondida object (105)	3		16	1
452	2023-08-27 22:23:51.655037-03	104	QuestaoRespondida object (104)	3		16	1
453	2023-08-27 22:23:51.659852-03	103	QuestaoRespondida object (103)	3		16	1
454	2023-08-27 22:23:51.665122-03	102	QuestaoRespondida object (102)	3		16	1
455	2023-08-27 22:23:51.66794-03	101	QuestaoRespondida object (101)	3		16	1
456	2023-08-27 22:23:51.670598-03	100	QuestaoRespondida object (100)	3		16	1
457	2023-08-27 22:23:51.673241-03	99	QuestaoRespondida object (99)	3		16	1
458	2023-08-27 22:23:51.675685-03	98	QuestaoRespondida object (98)	3		16	1
459	2023-08-27 22:23:51.678307-03	97	QuestaoRespondida object (97)	3		16	1
460	2023-08-27 22:23:51.682657-03	96	QuestaoRespondida object (96)	3		16	1
461	2023-08-27 22:23:51.687232-03	95	QuestaoRespondida object (95)	3		16	1
462	2023-08-27 22:23:51.691235-03	94	QuestaoRespondida object (94)	3		16	1
463	2023-08-27 22:23:51.693751-03	93	QuestaoRespondida object (93)	3		16	1
464	2023-08-27 22:23:51.696199-03	92	QuestaoRespondida object (92)	3		16	1
465	2023-08-27 22:23:51.698616-03	91	QuestaoRespondida object (91)	3		16	1
466	2023-08-27 22:23:51.701192-03	90	QuestaoRespondida object (90)	3		16	1
467	2023-08-27 22:23:51.704077-03	89	QuestaoRespondida object (89)	3		16	1
468	2023-08-27 22:23:51.7069-03	88	QuestaoRespondida object (88)	3		16	1
469	2023-08-27 22:23:51.71326-03	87	QuestaoRespondida object (87)	3		16	1
470	2023-08-27 22:23:51.717294-03	86	QuestaoRespondida object (86)	3		16	1
471	2023-08-27 22:23:51.719959-03	85	QuestaoRespondida object (85)	3		16	1
472	2023-08-27 22:23:51.722439-03	84	QuestaoRespondida object (84)	3		16	1
473	2023-08-27 22:23:51.725949-03	83	QuestaoRespondida object (83)	3		16	1
474	2023-08-27 22:23:51.732045-03	82	QuestaoRespondida object (82)	3		16	1
475	2023-08-27 22:23:51.738316-03	81	QuestaoRespondida object (81)	3		16	1
476	2023-08-27 22:23:51.742583-03	80	QuestaoRespondida object (80)	3		16	1
477	2023-08-27 22:23:51.748398-03	79	QuestaoRespondida object (79)	3		16	1
478	2023-08-27 22:23:51.751297-03	78	QuestaoRespondida object (78)	3		16	1
479	2023-08-27 22:23:51.753977-03	77	QuestaoRespondida object (77)	3		16	1
480	2023-08-27 22:23:51.756467-03	76	QuestaoRespondida object (76)	3		16	1
481	2023-08-27 22:23:51.762089-03	75	QuestaoRespondida object (75)	3		16	1
482	2023-08-27 22:23:51.767109-03	74	QuestaoRespondida object (74)	3		16	1
483	2023-08-27 22:23:51.769798-03	73	QuestaoRespondida object (73)	3		16	1
484	2023-08-27 22:23:51.772336-03	72	QuestaoRespondida object (72)	3		16	1
485	2023-08-27 22:23:51.77619-03	71	QuestaoRespondida object (71)	3		16	1
486	2023-08-27 22:23:51.782254-03	70	QuestaoRespondida object (70)	3		16	1
487	2023-08-27 22:23:51.785237-03	69	QuestaoRespondida object (69)	3		16	1
488	2023-08-27 22:23:51.788557-03	68	QuestaoRespondida object (68)	3		16	1
489	2023-08-27 22:23:51.793084-03	67	QuestaoRespondida object (67)	3		16	1
490	2023-08-27 22:23:51.79928-03	66	QuestaoRespondida object (66)	3		16	1
491	2023-08-27 22:23:51.803321-03	65	QuestaoRespondida object (65)	3		16	1
492	2023-08-27 22:23:51.805843-03	64	QuestaoRespondida object (64)	3		16	1
493	2023-08-27 22:23:51.809973-03	63	QuestaoRespondida object (63)	3		16	1
494	2023-08-27 22:23:51.814969-03	62	QuestaoRespondida object (62)	3		16	1
495	2023-08-27 22:23:51.817552-03	61	QuestaoRespondida object (61)	3		16	1
496	2023-08-27 22:23:51.82141-03	60	QuestaoRespondida object (60)	3		16	1
497	2023-08-27 22:23:51.825326-03	59	QuestaoRespondida object (59)	3		16	1
498	2023-08-27 22:23:51.830276-03	58	QuestaoRespondida object (58)	3		16	1
499	2023-08-27 22:23:51.833245-03	57	QuestaoRespondida object (57)	3		16	1
500	2023-08-27 22:23:51.835633-03	56	QuestaoRespondida object (56)	3		16	1
501	2023-08-27 22:23:51.837975-03	55	QuestaoRespondida object (55)	3		16	1
502	2023-08-27 22:23:51.840298-03	54	QuestaoRespondida object (54)	3		16	1
503	2023-08-27 22:23:51.842596-03	53	QuestaoRespondida object (53)	3		16	1
504	2023-08-27 22:23:51.845041-03	52	QuestaoRespondida object (52)	3		16	1
505	2023-08-27 22:23:51.847494-03	51	QuestaoRespondida object (51)	3		16	1
506	2023-08-27 22:23:51.849768-03	50	QuestaoRespondida object (50)	3		16	1
507	2023-08-27 22:23:51.852265-03	49	QuestaoRespondida object (49)	3		16	1
508	2023-08-27 22:23:51.854981-03	48	QuestaoRespondida object (48)	3		16	1
509	2023-08-27 22:23:51.858338-03	47	QuestaoRespondida object (47)	3		16	1
510	2023-08-27 22:23:51.863392-03	46	QuestaoRespondida object (46)	3		16	1
511	2023-08-27 22:23:51.867684-03	45	QuestaoRespondida object (45)	3		16	1
512	2023-08-27 22:23:51.870212-03	44	QuestaoRespondida object (44)	3		16	1
513	2023-08-27 22:23:51.872649-03	43	QuestaoRespondida object (43)	3		16	1
514	2023-08-27 22:23:51.875918-03	42	QuestaoRespondida object (42)	3		16	1
515	2023-08-27 22:23:51.881407-03	41	QuestaoRespondida object (41)	3		16	1
516	2023-08-27 22:23:51.884285-03	40	QuestaoRespondida object (40)	3		16	1
517	2023-08-27 22:23:51.886803-03	39	QuestaoRespondida object (39)	3		16	1
518	2023-08-27 22:23:51.88931-03	38	QuestaoRespondida object (38)	3		16	1
519	2023-08-27 22:23:51.892511-03	37	QuestaoRespondida object (37)	3		16	1
520	2023-08-27 22:23:51.898057-03	36	QuestaoRespondida object (36)	3		16	1
521	2023-08-27 22:23:51.902171-03	35	QuestaoRespondida object (35)	3		16	1
522	2023-08-27 22:23:51.904743-03	34	QuestaoRespondida object (34)	3		16	1
523	2023-08-27 22:23:51.908268-03	33	QuestaoRespondida object (33)	3		16	1
524	2023-08-27 22:23:51.914695-03	32	QuestaoRespondida object (32)	3		16	1
525	2023-08-27 22:23:51.917371-03	31	QuestaoRespondida object (31)	3		16	1
526	2023-08-27 22:23:51.920018-03	30	QuestaoRespondida object (30)	3		16	1
527	2023-08-27 22:23:51.922585-03	29	QuestaoRespondida object (29)	3		16	1
528	2023-08-27 22:23:51.926254-03	28	QuestaoRespondida object (28)	3		16	1
529	2023-08-27 22:23:51.931168-03	27	QuestaoRespondida object (27)	3		16	1
530	2023-08-27 22:23:51.935176-03	26	QuestaoRespondida object (26)	3		16	1
531	2023-08-27 22:23:51.937974-03	25	QuestaoRespondida object (25)	3		16	1
532	2023-08-27 22:23:51.941952-03	24	QuestaoRespondida object (24)	3		16	1
533	2023-08-27 22:23:51.946624-03	23	QuestaoRespondida object (23)	3		16	1
534	2023-08-27 22:23:51.9501-03	22	QuestaoRespondida object (22)	3		16	1
535	2023-08-27 22:23:51.952382-03	21	QuestaoRespondida object (21)	3		16	1
536	2023-08-27 22:23:51.955038-03	20	QuestaoRespondida object (20)	3		16	1
537	2023-08-27 22:24:01.403863-03	19	QuestaoRespondida object (19)	3		16	1
538	2023-08-27 22:24:01.409456-03	18	QuestaoRespondida object (18)	3		16	1
539	2023-08-27 22:24:01.414469-03	17	QuestaoRespondida object (17)	3		16	1
540	2023-08-27 22:24:01.417325-03	16	QuestaoRespondida object (16)	3		16	1
541	2023-08-27 22:24:01.420501-03	15	QuestaoRespondida object (15)	3		16	1
542	2023-08-27 22:24:01.427226-03	14	QuestaoRespondida object (14)	3		16	1
543	2023-08-27 22:24:01.432627-03	13	QuestaoRespondida object (13)	3		16	1
544	2023-08-27 22:24:01.437506-03	12	QuestaoRespondida object (12)	3		16	1
545	2023-08-27 22:24:01.441849-03	11	QuestaoRespondida object (11)	3		16	1
546	2023-08-27 22:24:01.447636-03	10	QuestaoRespondida object (10)	3		16	1
547	2023-08-27 22:24:01.450428-03	9	QuestaoRespondida object (9)	3		16	1
548	2023-08-27 22:24:01.452984-03	8	QuestaoRespondida object (8)	3		16	1
549	2023-08-27 22:24:01.457197-03	7	QuestaoRespondida object (7)	3		16	1
550	2023-08-27 22:24:01.462027-03	6	QuestaoRespondida object (6)	3		16	1
551	2023-08-27 22:24:01.466298-03	5	QuestaoRespondida object (5)	3		16	1
552	2023-08-27 22:24:01.468945-03	4	QuestaoRespondida object (4)	3		16	1
553	2023-08-27 22:24:01.47155-03	3	QuestaoRespondida object (3)	3		16	1
554	2023-08-27 22:24:01.475748-03	2	QuestaoRespondida object (2)	3		16	1
555	2023-08-27 22:24:01.480248-03	1	QuestaoRespondida object (1)	3		16	1
556	2023-09-06 00:53:09.430498-03	18	18 - None	3		11	1
557	2023-09-06 00:53:09.436541-03	19	19 - None	3		11	1
558	2023-09-06 00:53:09.439379-03	21	21 - None	3		11	1
559	2023-09-06 00:55:28.90375-03	25	25 - None	3		11	1
560	2023-09-06 00:56:42.07472-03	27	27 - None	3		11	1
561	2023-09-06 00:58:39.438899-03	29	29 - None	3		11	1
562	2023-09-06 01:03:43.449415-03	31	31 - None	3		11	1
563	2023-09-06 13:20:58.070162-03	15	QuestaoRespondida object (15)	3		16	1
564	2023-09-06 13:20:58.075182-03	14	QuestaoRespondida object (14)	3		16	1
565	2023-09-06 13:20:58.080011-03	13	QuestaoRespondida object (13)	3		16	1
566	2023-09-06 13:20:58.08451-03	12	QuestaoRespondida object (12)	3		16	1
567	2023-09-06 13:20:58.089419-03	11	QuestaoRespondida object (11)	3		16	1
568	2023-09-06 13:20:58.09557-03	10	QuestaoRespondida object (10)	3		16	1
569	2023-09-06 13:20:58.100602-03	9	QuestaoRespondida object (9)	3		16	1
570	2023-09-06 13:20:58.107236-03	8	QuestaoRespondida object (8)	3		16	1
571	2023-09-06 13:20:58.114109-03	7	QuestaoRespondida object (7)	3		16	1
572	2023-09-06 13:20:58.117966-03	6	QuestaoRespondida object (6)	3		16	1
573	2023-09-06 13:20:58.121015-03	5	QuestaoRespondida object (5)	3		16	1
574	2023-09-06 13:20:58.123844-03	4	QuestaoRespondida object (4)	3		16	1
575	2023-09-06 13:20:58.127882-03	3	QuestaoRespondida object (3)	3		16	1
576	2023-09-06 13:20:58.130945-03	2	QuestaoRespondida object (2)	3		16	1
577	2023-09-06 13:20:58.133717-03	1	QuestaoRespondida object (1)	3		16	1
578	2023-09-06 13:23:36.636957-03	32	32 - None	3		11	1
579	2023-09-06 14:10:51.94525-03	22	OpcaoImagem object (22)	3		22	1
580	2023-09-06 14:10:51.952143-03	21	OpcaoImagem object (21)	3		22	1
581	2023-09-06 14:10:51.957183-03	20	OpcaoImagem object (20)	3		22	1
582	2023-09-06 14:10:51.961132-03	19	OpcaoImagem object (19)	3		22	1
583	2023-09-06 14:10:51.965395-03	18	OpcaoImagem object (18)	3		22	1
584	2023-09-06 14:10:51.970863-03	17	OpcaoImagem object (17)	3		22	1
585	2023-09-06 14:10:51.974626-03	16	OpcaoImagem object (16)	3		22	1
586	2023-09-06 14:10:51.978134-03	15	OpcaoImagem object (15)	3		22	1
587	2023-09-06 14:10:51.981789-03	14	OpcaoImagem object (14)	3		22	1
588	2023-09-06 14:10:51.987975-03	13	OpcaoImagem object (13)	3		22	1
589	2023-09-06 14:10:51.991925-03	12	OpcaoImagem object (12)	3		22	1
590	2023-09-06 14:10:51.995585-03	11	OpcaoImagem object (11)	3		22	1
591	2023-09-06 14:10:51.999508-03	10	OpcaoImagem object (10)	3		22	1
592	2023-09-06 14:10:52.002881-03	9	OpcaoImagem object (9)	3		22	1
593	2023-09-06 14:10:52.006313-03	8	OpcaoImagem object (8)	3		22	1
594	2023-09-06 14:10:52.009733-03	7	OpcaoImagem object (7)	3		22	1
595	2023-09-06 14:10:52.013301-03	6	OpcaoImagem object (6)	3		22	1
596	2023-09-06 14:11:10.525927-03	1	1 - Fácil	3		11	1
597	2023-09-06 14:11:10.533245-03	2	2 - Fácil	3		11	1
598	2023-09-06 14:11:10.535885-03	3	3 - Médio	3		11	1
599	2023-09-06 14:11:10.538575-03	4	4 - Médio	3		11	1
600	2023-09-06 14:11:10.541271-03	5	5 - Difícil	3		11	1
601	2023-09-06 14:11:10.54473-03	6	6 - Médio	3		11	1
602	2023-09-06 14:11:10.547753-03	7	7 - Difícil	3		11	1
603	2023-09-06 14:11:10.55056-03	8	8 - Médio	3		11	1
604	2023-09-06 14:11:10.552968-03	9	9 - Médio	3		11	1
605	2023-09-06 14:11:10.555455-03	10	10 - Médio	3		11	1
606	2023-09-06 14:11:10.558061-03	11	11 - Médio	3		11	1
607	2023-09-06 14:11:10.56119-03	12	12 - Difícil	3		11	1
608	2023-09-06 14:11:10.563849-03	13	13 - Fácil	3		11	1
609	2023-09-06 14:11:10.566333-03	15	15 - None	3		11	1
610	2023-09-06 14:11:10.568895-03	16	16 - None	3		11	1
611	2023-09-06 14:11:10.571679-03	17	17 - None	3		11	1
612	2023-09-06 14:11:10.574194-03	34	34 - None	3		11	1
613	2023-09-06 14:11:10.577235-03	35	35 - None	3		11	1
614	2023-09-06 14:11:10.579841-03	36	36 - None	3		11	1
615	2023-09-06 14:11:10.582221-03	37	37 - None	3		11	1
616	2023-09-06 14:11:10.584818-03	38	38 - None	3		11	1
617	2023-09-06 14:11:10.587535-03	39	39 - None	3		11	1
618	2023-09-06 14:11:10.589906-03	40	40 - None	3		11	1
619	2023-09-06 14:11:10.592443-03	41	41 - None	3		11	1
620	2023-09-06 14:11:10.595231-03	42	42 - None	3		11	1
621	2023-09-06 14:11:10.597803-03	43	43 - None	3		11	1
622	2023-09-06 14:11:10.600369-03	44	44 - None	3		11	1
623	2023-09-06 14:11:10.602771-03	45	45 - None	3		11	1
624	2023-09-06 14:11:10.605205-03	46	46 - None	3		11	1
625	2023-09-06 14:11:10.607688-03	47	47 - None	3		11	1
626	2023-09-06 14:11:10.610687-03	48	48 - None	3		11	1
627	2023-09-06 14:11:10.613306-03	49	49 - None	3		11	1
628	2023-09-06 14:11:10.615747-03	50	50 - None	3		11	1
629	2023-09-06 14:21:00.609355-03	19	Permutação ; - Matemática	3		10	1
630	2023-09-06 14:21:00.614336-03	18	Permutação; - Matemática	3		10	1
631	2023-09-06 14:21:00.616806-03	17	Combinação; - Matemática	3		10	1
632	2023-09-06 14:21:00.619719-03	16	Movimentos, Classificação e Função Horária - Física	3		10	1
633	2023-09-06 14:21:00.622793-03	15	Movimento Circular Uniforme - Física	3		10	1
634	2023-09-06 14:21:00.627825-03	14	Interpretação de texto - Português	3		10	1
635	2023-09-06 14:21:00.630786-03	13	Hubble - Física	3		10	1
636	2023-09-06 14:21:00.633447-03	12	Impacto e Colisões - Física	3		10	1
637	2023-09-06 14:21:00.635946-03	11	Forças e Aceleração - Física	3		10	1
638	2023-09-06 14:21:00.63868-03	10	Análise de Dados - Matemática	3		10	1
639	2023-09-06 14:21:00.641708-03	9	Movimento - Matemática	3		10	1
640	2023-09-06 14:21:00.646313-03	8	Eletricidade - Física	3		10	1
641	2023-09-06 14:21:00.64888-03	7	Unidades de medida - Matemática	3		10	1
642	2023-09-06 14:21:00.651425-03	6	Tempo - Matemática	3		10	1
643	2023-09-06 14:21:00.653996-03	5	Analise de Gráfico - Matemática	3		10	1
644	2023-09-06 14:21:00.657797-03	3	Geometria Analitica - Matemática	3		10	1
645	2023-09-06 14:21:00.664735-03	2	Eletrodinâmica - Física	3		10	1
646	2023-09-06 14:21:00.66786-03	1	Geometria Plana - Matemática	3		10	1
647	2023-09-06 14:37:55.210687-03	51	51 - None	3		11	1
648	2023-09-06 14:37:55.214009-03	52	52 - None	3		11	1
649	2023-09-06 14:37:55.216545-03	53	53 - None	3		11	1
650	2023-09-06 14:37:55.219851-03	54	54 - None	3		11	1
651	2023-09-06 14:37:55.22653-03	55	55 - None	3		11	1
652	2023-09-06 14:37:55.229619-03	56	56 - None	3		11	1
653	2023-09-06 14:38:01.64808-03	22	Permutação ; - Matemática	3		10	1
654	2023-09-06 14:38:01.651385-03	21	Permutação; - Matemática	3		10	1
655	2023-09-06 14:38:01.655206-03	20	Combinação; - Matemática	3		10	1
656	2023-09-06 14:41:23.60601-03	57	57 - None	3		11	1
657	2023-09-06 14:41:23.609742-03	58	58 - None	3		11	1
658	2023-09-06 14:41:23.615238-03	59	59 - None	3		11	1
659	2023-09-06 14:41:23.618146-03	60	60 - None	3		11	1
660	2023-09-06 14:41:23.620753-03	61	61 - None	3		11	1
661	2023-09-06 14:41:28.60477-03	30	Análise Combinatória - Permutação - Matemática	3		6	1
662	2023-09-06 14:41:28.613506-03	29	Análise Combinatória - Combinação - Matemática	3		6	1
663	2023-09-06 14:41:35.109467-03	4	Roberto - 2023-08-28 02:06:31.859084+00:00	3		13	1
664	2023-09-06 14:41:35.116931-03	3	Roberto - 2023-08-28 01:36:05.996965+00:00	3		13	1
665	2023-09-06 14:41:35.119697-03	2	Roberto - 2023-08-28 01:29:26.807634+00:00	3		13	1
666	2023-09-06 14:41:35.122425-03	1	Roberto - 2023-08-28 01:23:07.218330+00:00	3		13	1
667	2023-09-06 14:41:48.08224-03	24	Permutação - Matemática	3		10	1
668	2023-09-06 14:41:48.088755-03	23	Combinação - Matemática	3		10	1
669	2023-09-06 14:50:08.098907-03	62	62 - None	3		11	1
670	2023-09-06 14:50:08.110772-03	63	63 - None	3		11	1
671	2023-09-06 14:50:08.142887-03	64	64 - None	3		11	1
672	2023-09-06 14:50:08.176797-03	65	65 - None	3		11	1
673	2023-09-06 14:50:08.212666-03	66	66 - None	3		11	1
674	2023-09-06 14:52:24.710848-03	43	OpcaoImagem object (43)	3		22	1
675	2023-09-06 14:52:24.714205-03	42	OpcaoImagem object (42)	3		22	1
676	2023-09-06 14:52:24.717133-03	41	OpcaoImagem object (41)	3		22	1
677	2023-09-06 14:52:24.721775-03	40	OpcaoImagem object (40)	3		22	1
678	2023-09-06 14:52:24.726142-03	39	OpcaoImagem object (39)	3		22	1
679	2023-09-06 14:52:29.510688-03	67	67 - None	3		11	1
680	2023-09-06 14:52:29.513823-03	68	68 - None	3		11	1
681	2023-09-06 14:52:29.516601-03	69	69 - None	3		11	1
682	2023-09-06 14:52:29.520616-03	70	70 - None	3		11	1
683	2023-09-06 14:52:29.524846-03	71	71 - None	3		11	1
684	2023-09-06 14:56:22.523592-03	48	OpcaoImagem object (48)	3		22	1
685	2023-09-06 14:56:22.528273-03	47	OpcaoImagem object (47)	3		22	1
686	2023-09-06 14:56:22.531645-03	46	OpcaoImagem object (46)	3		22	1
687	2023-09-06 14:56:22.535755-03	45	OpcaoImagem object (45)	3		22	1
688	2023-09-06 14:56:22.539555-03	44	OpcaoImagem object (44)	3		22	1
689	2023-09-06 14:56:33.958379-03	72	72 - None	3		11	1
690	2023-09-06 14:56:33.961316-03	73	73 - None	3		11	1
691	2023-09-06 14:56:33.964549-03	74	74 - None	3		11	1
692	2023-09-06 14:56:33.969411-03	75	75 - None	3		11	1
693	2023-09-06 14:56:33.972047-03	76	76 - None	3		11	1
694	2023-09-06 17:55:49.681531-03	77	77 - None	3		11	1
695	2023-09-06 17:55:49.692914-03	78	78 - None	3		11	1
696	2023-09-06 17:55:49.696761-03	79	79 - None	3		11	1
697	2023-09-06 17:55:49.703319-03	80	80 - None	3		11	1
698	2023-09-06 17:55:49.708958-03	81	81 - None	3		11	1
699	2023-09-06 17:55:55.408366-03	32	Análise Combinatória - Permutação - Matemática	3		6	1
700	2023-09-06 17:55:55.412333-03	31	Análise Combinatória - Combinação - Matemática	3		6	1
701	2023-09-06 18:03:20.612267-03	83	83 - None	3		11	1
702	2023-09-06 18:11:22.627655-03	1	1 - None	3		11	1
703	2023-09-06 18:11:54.261258-03	1	OpcaoImagem object (1)	3		22	1
704	2023-09-06 18:11:59.786618-03	1	1 - None	3		11	1
705	2023-09-06 18:12:36.50284-03	1	1 - None	3		11	1
706	2023-09-06 18:14:22.965331-03	6	OpcaoImagem object (6)	3		22	1
707	2023-09-06 18:14:22.969699-03	5	OpcaoImagem object (5)	3		22	1
708	2023-09-06 18:14:22.974468-03	4	OpcaoImagem object (4)	3		22	1
709	2023-09-06 18:14:22.978022-03	3	OpcaoImagem object (3)	3		22	1
710	2023-09-06 18:14:22.980619-03	2	OpcaoImagem object (2)	3		22	1
711	2023-09-06 18:14:29.19026-03	2	2 - 226124	3		11	1
712	2023-09-06 18:14:29.193635-03	3	3 - 222436	3		11	1
713	2023-09-06 18:14:29.196209-03	4	4 - 222478	3		11	1
714	2023-09-06 18:14:29.198817-03	5	5 - 227831	3		11	1
715	2023-09-06 18:14:29.203034-03	6	6 - 222501	3		11	1
716	2023-09-06 18:23:09.087506-03	1	OpcaoImagem object (1)	3		22	1
717	2023-09-06 18:23:09.092658-03	2	OpcaoImagem object (2)	3		22	1
718	2023-09-06 18:23:09.096677-03	3	OpcaoImagem object (3)	3		22	1
719	2023-09-06 18:23:09.103983-03	4	OpcaoImagem object (4)	3		22	1
720	2023-09-06 18:23:09.107549-03	5	OpcaoImagem object (5)	3		22	1
721	2023-09-06 18:23:13.258568-03	1	1 - 226124	3		11	1
722	2023-09-06 18:23:13.263125-03	2	2 - 222436	3		11	1
723	2023-09-06 18:23:13.26686-03	3	3 - 222478	3		11	1
724	2023-09-06 18:23:13.271609-03	4	4 - 227831	3		11	1
725	2023-09-06 18:23:13.274566-03	5	5 - 222501	3		11	1
726	2023-09-06 19:45:24.948262-03	1	1 - 226124	3		11	1
727	2023-09-06 19:45:24.958204-03	2	2 - 222436	3		11	1
728	2023-09-06 19:45:24.961616-03	3	3 - 222478	3		11	1
729	2023-09-06 19:45:24.965191-03	4	4 - 227831	3		11	1
730	2023-09-06 19:45:24.972161-03	5	5 - 222501	3		11	1
731	2023-09-06 19:45:24.976405-03	6	6 - 160181	3		11	1
732	2023-09-06 19:45:24.979078-03	7	7 - 144133	3		11	1
733	2023-09-06 19:45:24.981764-03	8	8 - 222359	3		11	1
734	2023-09-06 19:45:24.986563-03	9	9 - 160458	3		11	1
735	2023-09-06 19:45:24.989632-03	10	10 - 222351	3		11	1
736	2023-09-06 19:45:24.992032-03	11	11 - 186841	3		11	1
737	2023-09-06 19:50:42.314157-03	1	1 - 222351	3		11	1
738	2023-09-06 19:50:42.318994-03	2	2 - 186841	3		11	1
739	2023-09-06 19:55:10.59679-03	3	3 - 160181	3		11	1
740	2023-09-06 19:55:10.601663-03	4	4 - 144133	3		11	1
741	2023-09-06 19:55:10.608621-03	5	5 - 222359	3		11	1
742	2023-09-06 19:55:10.613467-03	6	6 - 160458	3		11	1
743	2023-09-06 19:55:10.616176-03	7	7 - 222351	3		11	1
744	2023-09-06 19:55:10.619263-03	8	8 - 186841	3		11	1
745	2023-09-06 19:58:29.444289-03	1	1 - 160181	3		11	1
746	2023-09-06 19:58:29.453958-03	2	2 - 144133	3		11	1
747	2023-09-06 19:58:29.45685-03	3	3 - 222359	3		11	1
748	2023-09-06 19:58:29.459512-03	4	4 - 160458	3		11	1
749	2023-09-06 19:58:29.466168-03	5	5 - 222351	3		11	1
750	2023-09-06 19:58:29.470856-03	6	6 - 186841	3		11	1
751	2023-09-06 20:14:48.595211-03	1	OpcaoImagem object (1)	3		22	1
752	2023-09-06 20:14:48.603083-03	2	OpcaoImagem object (2)	3		22	1
753	2023-09-06 20:14:48.608331-03	3	OpcaoImagem object (3)	3		22	1
754	2023-09-06 20:14:48.615083-03	4	OpcaoImagem object (4)	3		22	1
755	2023-09-06 20:14:48.620924-03	5	OpcaoImagem object (5)	3		22	1
756	2023-09-06 20:14:48.626053-03	6	OpcaoImagem object (6)	3		22	1
757	2023-09-06 20:14:58.92886-03	1	1 - 160181	3		11	1
758	2023-09-06 20:14:58.932056-03	2	2 - 144133	3		11	1
759	2023-09-06 20:14:58.934977-03	3	3 - 222359	3		11	1
760	2023-09-06 20:14:58.938476-03	4	4 - 160458	3		11	1
761	2023-09-06 20:14:58.941555-03	5	5 - 222351	3		11	1
762	2023-09-06 20:14:58.944462-03	6	6 - 186841	3		11	1
763	2023-09-06 20:24:47.04073-03	13	13 - 226124	3		11	1
764	2023-09-06 20:29:21.313965-03	15	15 - 226124	3		11	1
765	2023-09-06 20:31:54.409438-03	17	17 - 226124	3		11	1
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2023-08-22 19:54:28.676538-03
2	contenttypes	0002_remove_content_type_name	2023-08-22 19:54:28.686525-03
3	auth	0001_initial	2023-08-22 19:54:28.759136-03
4	auth	0002_alter_permission_name_max_length	2023-08-22 19:54:28.77326-03
5	auth	0003_alter_user_email_max_length	2023-08-22 19:54:28.788446-03
6	auth	0004_alter_user_username_opts	2023-08-22 19:54:28.797202-03
7	auth	0005_alter_user_last_login_null	2023-08-22 19:54:28.805836-03
8	auth	0006_require_contenttypes_0002	2023-08-22 19:54:28.809269-03
9	auth	0007_alter_validators_add_error_messages	2023-08-22 19:54:28.815238-03
10	auth	0008_alter_user_username_max_length	2023-08-22 19:54:28.821108-03
11	auth	0009_alter_user_last_name_max_length	2023-08-22 19:54:28.830537-03
12	auth	0010_alter_group_name_max_length	2023-08-22 19:54:28.837002-03
13	auth	0011_update_proxy_permissions	2023-08-22 19:54:28.842682-03
14	auth	0012_alter_user_first_name_max_length	2023-08-22 19:54:28.848454-03
15	usuarios	0001_initial	2023-08-22 19:54:28.934884-03
16	admin	0001_initial	2023-08-22 19:54:28.9684-03
17	admin	0002_logentry_remove_auto_add	2023-08-22 19:54:28.978059-03
18	admin	0003_logentry_add_action_flag_choices	2023-08-22 19:54:28.999433-03
20	materiais	0002_alter_nivel_peso	2023-08-22 19:54:29.076865-03
21	materiais	0003_alter_nivel_options_alter_questoes_options_and_more	2023-08-22 19:54:29.092425-03
22	materiais	0004_questoes_opcao_correta	2023-08-22 19:54:29.103881-03
23	materiais	0005_conteudo_questoesprova_provarespondida_and_more	2023-08-22 19:54:29.165292-03
24	materiais	0006_rename_questoes_questao_provarespondida_resposta_and_more	2023-08-22 19:54:29.28882-03
25	materiais	0007_alter_provacompleta_respostas_and_more	2023-08-22 19:54:29.339773-03
26	materiais	0008_remove_materia_submateria_remove_questao_materia_and_more	2023-08-22 19:54:29.415185-03
27	materiais	0009_alter_submateria_materia	2023-08-22 19:54:29.452718-03
28	materiais	0010_conteudo_sub_materia	2023-08-22 19:54:29.476744-03
29	materiais	0011_remove_questao_sub_materia_alter_questao_imagem	2023-08-22 19:54:29.495943-03
30	materiais	0012_remove_provacompleta_tipo_provacompleta_nota_and_more	2023-08-22 19:54:29.524102-03
31	materiais	0013_alter_questoesprova_options_alter_submateria_options_and_more	2023-08-22 19:54:29.566602-03
32	materiais	0014_remove_questao_tipo	2023-08-22 19:54:29.573452-03
33	materiais	0015_tipos	2023-08-22 19:54:29.586125-03
34	materiais	0016_rename_tipos_tipo	2023-08-22 19:54:29.607804-03
35	materiais	0017_questao_tipo	2023-08-22 19:54:29.638586-03
36	sessions	0001_initial	2023-08-22 19:55:46.900124-03
37	usuarios	0002_account_is_aluno_alter_account_is_admin	2023-08-22 19:55:46.918965-03
38	usuarios	0003_alter_account_is_admin	2023-08-22 19:55:46.930089-03
39	usuarios	0004_mediageral	2023-08-22 19:55:46.957583-03
40	materiais	0001_initial	2023-08-22 20:41:50.789061-03
41	materiais	0002_remove_provacompleta_respostas_and_more	2023-08-22 22:02:45.893004-03
42	usuarios	0005_mediageral_data_calculada	2023-08-22 22:02:45.903542-03
43	materiais	0003_alter_provacompleta_tipos_alter_questao_nivel_and_more	2023-08-23 14:28:34.317507-03
44	materiais	0004_alter_provarespondida_resposta_alter_questao_nivel_and_more	2023-08-23 16:15:27.58369-03
45	materiais	0005_alter_conteudo_nome	2023-08-24 17:56:48.97705-03
46	materiais	0006_alter_conteudo_nome	2023-08-24 17:59:02.777688-03
47	usuarios	0006_alter_mediageral_options_and_more	2023-08-24 22:27:08.510168-03
48	usuarios	0007_alter_mediageral_data_calculada	2023-08-27 08:58:07.452461-03
49	materiais	0007_remove_questao_conteudo_questao_conteudo	2023-08-27 09:48:22.782025-03
50	materiais	0008_provacompleta_materias_alter_provacompleta_nota_and_more	2023-08-27 15:40:28.350969-03
51	materiais	0009_remove_provacompleta_materias	2023-08-27 15:45:50.06261-03
52	materiais	0010_simulado_remove_provacompleta_tipos_and_more	2023-08-27 17:06:49.177534-03
53	materiais	0011_provarespondida_simulado_simulado_materia	2023-08-27 17:59:50.397353-03
54	usuarios	0008_alter_account_cpf	2023-08-27 23:00:12.683898-03
55	materiais	0012_alter_simulado_materia	2023-08-29 21:39:51.178455-03
56	usuarios	0009_alter_account_telefone	2023-08-30 18:03:11.919219-03
57	usuarios	0010_alter_mediageral_media_ciencias_humanas_and_more	2023-08-30 22:19:58.33811-03
58	usuarios	0011_alter_mediageral_media_ciencias_humanas_and_more	2023-08-30 22:20:21.058817-03
59	usuarios	0012_notas_delete_mediageral	2023-08-31 16:16:09.140564-03
60	usuarios	0013_alter_notas_options_mediageral	2023-08-31 16:55:36.470906-03
61	usuarios	0014_account_is_professor_alter_account_is_aluno	2023-09-01 14:26:25.221161-03
62	usuarios	0015_account_is_verified	2023-09-01 15:12:53.534268-03
66	usuarios	0019_turma_codigo_alter_professor_alunos_and_more	2023-09-02 19:30:59.477707-03
67	usuarios	0020_alter_turma_codigo	2023-09-02 19:32:03.364368-03
68	usuarios	0021_remove_turma_codigo	2023-09-02 19:35:27.457314-03
71	usuarios	0021_alter_turma_nome	2023-09-02 19:44:24.977142-03
72	usuarios	0022_turma_criador	2023-09-03 08:21:10.261468-03
73	usuarios	0023_alter_turma_criador_alter_turma_professores	2023-09-03 08:24:05.5533-03
74	usuarios	0024_alter_turma_codigo_alter_turma_criador_and_more	2023-09-03 08:31:29.824183-03
75	usuarios	0025_alter_turma_criador	2023-09-03 09:36:04.479719-03
76	usuarios	0026_alter_turma_criador	2023-09-03 09:37:09.430923-03
79	usuarios	0016_account_is_newsletter	2023-09-03 09:40:33.29778-03
80	usuarios	0017_aluno_professor_turma	2023-09-03 09:40:33.491801-03
81	usuarios	0018_professor_alunos_professor_total_alunos	2023-09-03 09:40:33.550513-03
82	usuarios	0019_alter_professor_alunos_alter_professor_total_alunos_and_more	2023-09-03 09:40:33.609142-03
83	usuarios	0020_turma_codigo	2023-09-03 09:40:33.624787-03
84	usuarios	0021_turma_criador_alter_turma_codigo_alter_turma_nome_and_more	2023-09-03 09:40:33.682885-03
85	usuarios	0018_alter_turma_professores	2023-09-03 09:54:13.888521-03
86	usuarios	0019_alter_professor_alunos_alter_professor_total_alunos	2023-09-03 09:59:23.006516-03
87	usuarios	0021_alter_mediageral_media_ciencias_humanas_and_more	2023-09-04 23:09:12.547848-03
88	materiais	0013_questao_indentificador_unico	2023-09-05 22:38:11.793323-03
89	materiais	0014_rename_imagem_questao_imagem_enunciado_opcaoimagem	2023-09-06 00:31:11.575378-03
90	materiais	0015_rename_indentificador_unico_questao_identificador_unico	2023-09-06 13:23:15.28544-03
91	materiais	0016_alter_opcaoimagem_options	2023-09-07 19:13:51.633637-03
92	materiais	0017_remove_provacompleta_usuario_and_more	2023-09-08 19:08:05.243634-03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
28d31rnw0wl57idj6lmxnz5kqllhwf5f	.eJxVjksOgjAURffSsSG8tpTC0LkrMKZ5_UkVKaHFiXHvlgQTnd3cz8l9EYVrHtSa3KKCJT0Bcvj1NJq7m7bA3nC6xsrEKS9BV1ul2tNUnaJ143Hv_gEGTENZe9eh4S3TUgCj0KLmlgrw4Bu01CDHmtO6liBcZ1grHWi0zlAvnQfR6ALNYY5qXuITCy-FxzqijcX_yvJfjSFl0p8JI5f3B16BSVo:1qaQy3:LGxPiiep7YoTnwF5Avtc3QfOMc11Mz4TvY1Ug1r67hY	2023-09-03 22:22:59.167371-03
qhytq5e2wxc58cijac2nqztth7htandz	e30:1qZc7I:hjH0hwpGlvIQtWqaDxJXDD8w-xSZ3cgYYlmzdRwBTbg	2023-09-01 16:05:08.881983-03
k7guwps559xh4v3kmqf5qt6cna5oldwa	e30:1qZcAR:1yZse8X5kOmCkNC9Ae6Pf9b3ziyTmCkd2mRdiq901uk	2023-09-01 16:08:23.747451-03
epdh1u5u1jw2mtevqjrsp3gw7n7qal8q	e30:1qZcBh:Dy-rp-6EzK5sc3BiYB7J2HfcygZrvyI35FQ_WhKmB-U	2023-09-01 16:09:41.713619-03
8vwo5o4meoln25ntpuy6od1n7u3axxy9	e30:1qZcCc:yhNZ96zQFmQrn_hxuFmVhV0dQBN8UwVHjZCaM2aq5Vc	2023-09-01 16:10:38.909715-03
bqpnguaztkkq7j8emhm17l3nhmwwcmsp	.eJxVjEEOwiAQRe_C2hCGUqAu3XsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3EWIE6_G2F8cN1BumO9NRlbXZeZ5K7Ig3Z5bYmfl8P9OyjYy7fOPGE0biBvYdDgkEzSFjLkEZOOaFAZrZQHy1McnGcgTBx19pzBjiTeH-lfOE0:1qZcDM:bU6eOie-QfsJeu-yzbEhRj-bv30v0Dnu3wwuB84yAlo	2023-09-01 16:11:24.054616-03
y64jh4p43difvpjoh1nxk3pyho5zffpc	.eJxVjEEOwiAQRe_C2hCGUqAu3XsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3EWIE6_G2F8cN1BumO9NRlbXZeZ5K7Ig3Z5bYmfl8P9OyjYy7fOPGE0biBvYdDgkEzSFjLkEZOOaFAZrZQHy1McnGcgTBx19pzBjiTeH-lfOE0:1qZcMc:LF_YotCZDAV3_hjo6rQQH5doYOrkhzA6dTcc52JUC8k	2023-09-01 16:20:58.211651-03
xn673y48lrf423p2kt2z6jtqq1dr7l0f	.eJxVjEEOwiAQRe_C2hCGUqAu3XsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3EWIE6_G2F8cN1BumO9NRlbXZeZ5K7Ig3Z5bYmfl8P9OyjYy7fOPGE0biBvYdDgkEzSFjLkEZOOaFAZrZQHy1McnGcgTBx19pzBjiTeH-lfOE0:1qa1MO:ou87ccpUc_mND9xAjk5ZRBf0VlaD_h27Xele_uKistU	2023-09-02 19:02:24.472585-03
e1kfu3hb5lnq2vr8rkpn9ytrg751jrp6	.eJxVjEEOwiAQRe_C2hCGUqAu3XsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3EWIE6_G2F8cN1BumO9NRlbXZeZ5K7Ig3Z5bYmfl8P9OyjYy7fOPGE0biBvYdDgkEzSFjLkEZOOaFAZrZQHy1McnGcgTBx19pzBjiTeH-lfOE0:1qa1cX:R2IQIzfuy6ve6HIJpL5r57sC2AUnzz4RIOF9GA9ncJM	2023-09-02 19:19:05.968443-03
27sp2mpp7asjfhrikedmivtd81ieho0l	.eJxVjEEOwiAQRe_C2hCGUqAu3XsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3EWIE6_G2F8cN1BumO9NRlbXZeZ5K7Ig3Z5bYmfl8P9OyjYy7fOPGE0biBvYdDgkEzSFjLkEZOOaFAZrZQHy1McnGcgTBx19pzBjiTeH-lfOE0:1qaES3:5T4BZ-Elnu30Ywvjx9L7C4o7eR_ip9g7QMeXY9Fl1qU	2023-09-03 09:01:07.362226-03
gj8ifjnyzajvj8lgm65o204an3nrl8yq	.eJxVjksOgjAURffSsSG8tpTC0LkrMKZ5_UkVKaHFiXHvlgQTnd3cz8l9EYVrHtSa3KKCJT0Bcvj1NJq7m7bA3nC6xsrEKS9BV1ul2tNUnaJ143Hv_gEGTENZe9eh4S3TUgCj0KLmlgrw4Bu01CDHmtO6liBcZ1grHWi0zlAvnQfR6ALNYY5qXuITCy-FxzqijcX_yvJfjSFl0p8JI5f3B16BSVo:1qaRe0:hBMdTW_Eqd01LfnqU5bSoDczhyhVvSmydaDE6qXbgxg	2023-09-03 23:06:20.166961-03
82jx5cez9jpexhjnjxkh5cwbxf51obt9	.eJxVjEEOwiAQRe_C2hCGUqAu3XsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3EWIE6_G2F8cN1BumO9NRlbXZeZ5K7Ig3Z5bYmfl8P9OyjYy7fOPGE0biBvYdDgkEzSFjLkEZOOaFAZrZQHy1McnGcgTBx19pzBjiTeH-lfOE0:1qdLVO:YQLlcxpP5TUO8jDEW8-q0xBNzwxCnpNtKf2Pq4gyeR0	2023-09-11 23:09:26.72044-03
fvgldiubrvean87iyfvr4kkwr42cvoow	.eJxVjEEOwiAQRe_C2hCGUqAu3XsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3EWIE6_G2F8cN1BumO9NRlbXZeZ5K7Ig3Z5bYmfl8P9OyjYy7fOPGE0biBvYdDgkEzSFjLkEZOOaFAZrZQHy1McnGcgTBx19pzBjiTeH-lfOE0:1qdvGS:LDKrAvZbzX8Vg04jLYD6IlQWOaIWYueCmN314KyqNP0	2023-09-13 13:20:24.338878-03
6zxxqv59d3klqhny4ch6z0ov1hlit84e	.eJxVjEEOwiAQRe_C2hCGUqAu3XsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3EWIE6_G2F8cN1BumO9NRlbXZeZ5K7Ig3Z5bYmfl8P9OyjYy7fOPGE0biBvYdDgkEzSFjLkEZOOaFAZrZQHy1McnGcgTBx19pzBjiTeH-lfOE0:1qe1E7:4k1tojXUW_wYJJesZ8E6GCbrtiCeDSRrkwdmW66RGxw	2023-09-13 19:42:23.517884-03
\.


--
-- Data for Name: materiais_materia; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_materia (id, nome) FROM stdin;
2	Educação Física
3	Português
4	História
5	Geografia
6	Física
7	Sociologia
8	Filosofia
9	Biologia
10	Química
11	Inglês
12	Literatura
13	Artes
1	Matemática
\.


--
-- Data for Name: materiais_submateria; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_submateria (id, nome, materia_id) FROM stdin;
25	Combinação	1
26	Permutação	1
27	Ácidos Nucléicos	9
28	Clonagem	9
29	Enzima	9
\.


--
-- Data for Name: materiais_conteudo; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_conteudo (id, nome, sub_materia_id) FROM stdin;
33	Análise Combinatória	25
34	Análise Combinatória	26
35	Bioquímica Celular	27
36	Bioquímica Celular	28
37	Bioquímica Celular	29
\.


--
-- Data for Name: materiais_nivel; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_nivel (id, nivel, peso) FROM stdin;
1	Fácil	40
2	Médio	15
3	Difícil	0.01
\.


--
-- Data for Name: materiais_questao; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_questao (id, enunciado, imagem_enunciado, opcoes, opcao_correta, nivel_id, identificador_unico) FROM stdin;
7	(ENEM MEC/2015)  \n  \nO formato das células de organismos pluricelulares é extremamente variado. Existem células discoides, como é o caso das hemácias, as que lembram uma estrela, como os neurônios, e ainda algumas alongadas, como as musculares.\n\nEm um mesmo organismo, a diferenciação dessas células ocorre por		["produzem mutações específicas.", "possuírem DNA mitocondrial diferentes.", "apresentarem conjunto de genes distintos.", "expressarem porções distintas do genoma.", "terem um número distinto de cromossomos."]	D	\N	160181
8	(ENEM MEC/2012)  \n  \nOs vegetais biossintetizam determinadas substâncias (por exemplo, alcaloides e flavonoides), cuja estrutura química e concentração variam num mesmo organismo em diferentes épocas do ano e estágios de desenvolvimento. Muitas dessas substâncias são produzidas para a adaptação do organismo às variações ambientais (radiação UV, temperatura, parasitas, herbívoros, estímulo a polinizadores etc.) ou fisiológicas (crescimento, envelhecimento etc.).\n\nAs variações qualitativa e quantitativa na produção dessas substâncias durante um ano são possíveis porque o material genético do indivíduo		["sofre constantes recombinações para adaptar-se.", "muda ao longo do ano e em diferentes fases da vida.", "cria novos genes para biossíntese de substâncias específicas.", "altera a sequência de bases nitrogenadas para criar novas substâncias.", "possui genes transcritos diferentemente de acordo com cada necessidade."]	E	\N	144133
9	(ENEM MEC/2020)  \n \nConsidere um banco de dados (Quadro 1) que apresenta sequências hipotéticas de DNA de duas áreas de extrativismo permitido (A1 e A2) e duas áreas de conservação (B1 e B2). Um órgão de fiscalização ambiental recebeu uma denúncia anônima de que cinco lojas moveleiras (1, 2, 3, 4 e 5) estariam comercializando produtos fabricados com madeira oriunda de áreas onde a extração é proibida. As sequências de DNA das amostras dos lotes apreendidos nas lojas moveleiras foram determinadas (Quadro 2) \n[IMG] . \n\n\n\n\n\n\n\n\n\n\n\n\n\nMIRANDA, N. E. O.; ALMEIDA JÚNIOR, E. B. A.; COLLEVATTI, R. G. A genética contra os crimes ambientais: identificação de madeira ilegal proveniente de unidades de conservação utilizando marcador molecular. Genética na Escola, v. 9, n. 2, 2014 (adaptado).\n\nQual loja moveleira comercializa madeira exclusivamente de forma ilegal?	questoes/questao_enunciado_222359..png	["1", "2", "3", "4", "5"]	E	\N	222359
10	(ENEM MEC/2015)  \n  \nA reprodução vegetativa de plantas por meio de estacas é um processo natural. O homem, observando esse processo, desenvolveu uma técnica para propagar plantas em escala comercial.\n\nA base genética dessa técnica é semelhante àquela presente no(a)		["transgenia.", "clonagem.", "hibridização.", "controle biológico.", "melhoramento genético."]	B	\N	160458
11	(ENEM MEC/2020)  \n \nO peróxido de hidrogênio é um produto secundário do metabolismo celular e apresenta algumas funções úteis, mas, quando em excesso, é prejudicial, gerando radicais que são tóxicos para as células. Para se defender, o organismo vivo utiliza a enzima catalase, que decompõe H2O2 em H2O e O2. A energia de reação de decomposição, quando na presença e ausência da catalase, está mostrada no gráfico. [IMG]\n\n\nDisponível em: www.pontociencia.org.br. Acesso em: 14 ago. 2013 (adaptado).\n\nNa situação descrita, o organismo utiliza a catalase porque ela	questoes/questao_enunciado_222351..png	["diminui a energia de ativação.", "permite maior rendimento da reação.", "diminui o valor da entalpia da reação.", "consome rapidamente o oxigênio do reagente.", "reage rapidamente com o peróxido de hidrogênio."]	A	\N	222351
12	(ENEM MEC/2017)  \n  \nSabendo-se que as enzimas podem ter sua atividade regulada por diferentes condições de temperatura e pH, foi realizado um experimento para testar as condições ótimas para a atividade de uma determinada enzima. Os resultados estão apresentados no gráfico. [IMG]\n\n\n\nEm relação ao funcionamento da enzima, os resultados obtidos indicam que o(a)	questoes/questao_enunciado_186841..png	["aumento do pH leva a uma atividade maior da enzima.", "temperatura baixa (10 ºC) é o principal inibidor da enzima.", "ambiente básico reduz a quantidade de enzima necessária na reação.", "ambiente básico reduz a quantidade de substrato metabolizado pela enzima.", "temperatura ótima de funcionamento da enzima é 30 ºC, independentemente do pH."]		\N	186841
18	(ENEM MEC/2021)  \n \nUma pessoa produzirá uma fantasia utilizando como materiais: 2 tipos de tecidos diferentes e 5 tipos distintos de pedras ornamentais. Essa pessoa tem à sua disposição 6 tecidos diferentes e 15 pedras ornamentais distintas.\n\nA quantidade de fantasias com materiais diferentes que podem ser produzidas é representada pela expressão		["[IMG]", "[IMG]", "[IMG]", "[IMG]", "[IMG]"]	A	\N	226124
19	(ENEM MEC/2020)  \n \nNos livros Harry Potter, um anagrama do nome do personagem “TOM MARVOLO RIDDLE” gerou a frase “I AM LORD VOLDEMORT”.\nSuponha que Harry quisesse formar todos os anagramas da frase “I AM POTTER”, de tal forma que as vogais e consoantes aparecessem sempre intercaladas, e sem considerar o espaçamento entre as letras.\n\nNessas condições, o número de anagramas formados é dado por		["9!", "4!5!", "24!5!", "[IMG]", "[IMG]"]		\N	222436
20	(ENEM MEC/2020)  \nConteudo: Análise Combinatória / Permutação ;\nEduardo deseja criar um e-mail utilizando um anagrama exclusivamente com as sete letras que compõem o seu nome, antes do símbolo @.\nO e-mail terá a forma *******@site.com.br e será de tal modo que as três letras “edu” apareçam sempre juntas e exatamente nessa ordem.\nEle sabe que o e-mail eduardo@site.com.br já foi criado por outro usuário e que qualquer outro agrupamento das letras do seu nome forma um e-mail que ainda não foi cadastrado.\n\nDe quantas maneiras Eduardo pode criar um e-mail desejado?		["59", "60", "118", "119", "120"]	D	\N	222478
21	(ENEM MEC/2022)  \n \nUm prédio, com 9 andares e 8 apartamentos de 2 quartos por andar, está com todos os seus apartamentos à venda. Os apartamentos são identificados por números formados por dois algarismos, sendo que a dezena indica o andar onde se encontra o apartamento, e a unidade, um algarismo de 1 a 8, que diferencia os apartamentos de um mesmo andar. Quanto à incidência de sol nos quartos desses apartamentos, constatam-se as seguintes características, em função de seus números de identificação:\n* naqueles que finalizam em 1 ou 2, ambos os quartos recebem sol apenas na parte da manhã;\n* naqueles que finalizam em 3, 4, 5 ou 6, apenas um dos quartos recebe sol na parte da manhã;\n* naqueles que finalizam em 7 ou 8, ambos os quartos recebem sol apenas na parte da tarde.\n\nUma pessoa pretende comprar 2 desses apartamentos em um mesmo andar, mas quer que, em ambos, pelo menos um dos quartos receba sol na parte da manhã.\n\nDe quantas maneiras diferentes essa pessoa poderá escolher 2 desses apartamentos para compra nas condições desejadas?		["[IMG]", "[IMG]", "[IMG]", "[IMG]", "[IMG]"]		\N	227831
22	(ENEM MEC/2020)  \nConteudo:  Análise Combinatória / Combinação;\nO governador de um estado propõe a ampliação de investimentos em segurança no transporte realizado por meio de trens. Um estudo para um projeto de lei prevê que se tenha a presença de três agentes mulheres, distribuídas entre os 6 vagões de uma composição, de forma que duas dessas agentes não estejam em vagões adjacentes, garantindo assim maior segurança aos usuários.\nDisponível em: www.sisgraph.com.br. Acesso em: 29 jan. 2015 (adaptado).\n\nA expressão que representa a quantidade de maneiras distintas das três agentes serem distribuídas nos vagões é		["[IMG]", "[IMG]", "[IMG]", "[IMG]", "[IMG]"]		\N	222501
\.


--
-- Data for Name: materiais_opcaoimagem; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_opcaoimagem (id, imagem_a, imagem_b, imagem_c, imagem_d, imagem_e, questao_id) FROM stdin;
7						7
8						8
9						9
10						10
11						11
12						12
16	questoes/questao_226124..png	questoes/questao_226124._UjUqNxq.png	questoes/questao_226124._O5nrfQS.png	questoes/questao_226124._9sMZhHa.png	questoes/questao_226124._WC2TtWF.png	18
17				questoes/questao_222436..png	questoes/questao_222436._VZmH4za.png	19
18						20
19	questoes/questao_227831..png	questoes/questao_227831._oIs1cYZ.png	questoes/questao_227831._alK4PAP.png	questoes/questao_227831._PuhUWnz.png	questoes/questao_227831._HV3uE1O.png	21
20	questoes/questao_222501..png	questoes/questao_222501._mouJLs6.png	questoes/questao_222501._2TsxQRr.png	questoes/questao_222501._kQXm0lw.png	questoes/questao_222501._E47Kyqw.png	22
\.


--
-- Data for Name: usuarios_aluno; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.usuarios_aluno (id, usuario_id) FROM stdin;
\.


--
-- Data for Name: materiais_provacompleta; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_provacompleta (id, nota, acertos, erros, ranking_piores_conteudos, ranking_melhores_conteudos, data_feita, acerto_dificuldade, aluno_id) FROM stdin;
\.


--
-- Data for Name: materiais_simulado; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_simulado (id, tipo) FROM stdin;
4	Linguagens e suas Tecnologias
3	Matemática
2	Ciências Humanas
1	Ciências da Natureza
\.


--
-- Data for Name: materiais_provarespondida; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_provarespondida (id, resposta, acerto, questao_id, prova_completa_id, simulado_id, aluno_id) FROM stdin;
\.


--
-- Data for Name: materiais_questao_conteudo; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_questao_conteudo (id, questao_id, conteudo_id) FROM stdin;
110	7	35
111	8	35
112	9	35
113	10	36
114	11	37
115	12	37
116	18	33
117	19	34
118	20	34
119	21	33
120	22	33
\.


--
-- Data for Name: materiais_questaorespondida; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_questaorespondida (id, questao_id, aluno_id) FROM stdin;
\.


--
-- Data for Name: materiais_questoesprova; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_questoesprova (id, questao_id) FROM stdin;
\.


--
-- Data for Name: materiais_simulado_materia; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_simulado_materia (id, simulado_id, materia_id) FROM stdin;
1	4	2
2	4	3
3	4	11
4	4	12
5	4	13
6	3	1
7	2	8
8	2	4
9	2	5
10	2	7
12	1	10
13	1	6
14	1	9
\.


--
-- Data for Name: materiais_tipo; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.materiais_tipo (id, nome) FROM stdin;
\.


--
-- Data for Name: usuarios_account_groups; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.usuarios_account_groups (id, account_id, group_id) FROM stdin;
\.


--
-- Data for Name: usuarios_account_user_permissions; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.usuarios_account_user_permissions (id, account_id, permission_id) FROM stdin;
\.


--
-- Data for Name: usuarios_mediageral; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.usuarios_mediageral (id, data_atualizada, media_matematica, media_ciencias_natureza, media_linguagens, media_ciencias_humanas, usuario_id) FROM stdin;
\.


--
-- Data for Name: usuarios_notas; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.usuarios_notas (id, data_calculada, nota_matematica, nota_ciencias_natureza, nota_linguagens, nota_ciencias_humanas, usuario_id) FROM stdin;
\.


--
-- Data for Name: usuarios_professor; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.usuarios_professor (id, usuario_id, alunos, total_alunos) FROM stdin;
\.


--
-- Data for Name: usuarios_turma; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.usuarios_turma (id, nome, data_criada, codigo, criador_id) FROM stdin;
\.


--
-- Data for Name: usuarios_turma_alunos; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.usuarios_turma_alunos (id, turma_id, aluno_id) FROM stdin;
\.


--
-- Data for Name: usuarios_turma_professores; Type: TABLE DATA; Schema: public; Owner: roberto
--

COPY public.usuarios_turma_professores (id, turma_id, professor_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 88, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 765, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 22, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 92, true);


--
-- Name: materiais_conteudo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_conteudo_id_seq', 37, true);


--
-- Name: materiais_materia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_materia_id_seq', 13, true);


--
-- Name: materiais_nivel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_nivel_id_seq', 6, true);


--
-- Name: materiais_opcaoimagem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_opcaoimagem_id_seq', 20, true);


--
-- Name: materiais_provacompleta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_provacompleta_id_seq', 4, true);


--
-- Name: materiais_provarespondida_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_provarespondida_id_seq', 20, true);


--
-- Name: materiais_questao_conteudo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_questao_conteudo_id_seq', 120, true);


--
-- Name: materiais_questao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_questao_id_seq', 22, true);


--
-- Name: materiais_questaorespondida_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_questaorespondida_id_seq', 15, true);


--
-- Name: materiais_questoesprova_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_questoesprova_id_seq', 1, false);


--
-- Name: materiais_simulado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_simulado_id_seq', 4, true);


--
-- Name: materiais_simulado_materia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_simulado_materia_id_seq', 14, true);


--
-- Name: materiais_submateria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_submateria_id_seq', 29, true);


--
-- Name: materiais_tipo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.materiais_tipo_id_seq', 1, false);


--
-- Name: usuarios_account_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.usuarios_account_groups_id_seq', 1, false);


--
-- Name: usuarios_account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.usuarios_account_id_seq', 4, true);


--
-- Name: usuarios_account_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.usuarios_account_user_permissions_id_seq', 1, false);


--
-- Name: usuarios_aluno_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.usuarios_aluno_id_seq', 1, false);


--
-- Name: usuarios_mediageral_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.usuarios_mediageral_id_seq', 1, false);


--
-- Name: usuarios_notas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.usuarios_notas_id_seq', 1, false);


--
-- Name: usuarios_professor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.usuarios_professor_id_seq', 1, false);


--
-- Name: usuarios_turma_alunos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.usuarios_turma_alunos_id_seq', 1, false);


--
-- Name: usuarios_turma_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.usuarios_turma_id_seq', 1, false);


--
-- Name: usuarios_turma_professores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roberto
--

SELECT pg_catalog.setval('public.usuarios_turma_professores_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

