PGDMP     2    
                {            hospital-db    15.1    15.1 O    _           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            `           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            a           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            b           1262    17072    hospital-db    DATABASE     �   CREATE DATABASE "hospital-db" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Finnish_Finland.1252';
    DROP DATABASE "hospital-db";
                postgres    false            �            1259    17073    appointment    TABLE       CREATE TABLE public.appointment (
    pat_id integer NOT NULL,
    start_time timestamp with time zone NOT NULL,
    emp_id integer,
    room_id integer,
    end_time timestamp with time zone NOT NULL,
    status character(1) DEFAULT 'A'::bpchar NOT NULL,
    cancel_rson text
);
    DROP TABLE public.appointment;
       public         heap    postgres    false            �            1259    17079    building    TABLE     �   CREATE TABLE public.building (
    bldg_id integer NOT NULL,
    bldg_address character varying(255) NOT NULL,
    hospital_id integer
);
    DROP TABLE public.building;
       public         heap    postgres    false            �            1259    17082    building_bldg_id_seq    SEQUENCE     �   CREATE SEQUENCE public.building_bldg_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.building_bldg_id_seq;
       public          postgres    false    215            c           0    0    building_bldg_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.building_bldg_id_seq OWNED BY public.building.bldg_id;
          public          postgres    false    216            �            1259    17083 
   department    TABLE     �   CREATE TABLE public.department (
    dept_id integer NOT NULL,
    dept_name character varying(255) NOT NULL,
    hospital_id integer
);
    DROP TABLE public.department;
       public         heap    postgres    false            �            1259    17086    department_dept_id_seq    SEQUENCE     �   CREATE SEQUENCE public.department_dept_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.department_dept_id_seq;
       public          postgres    false    217            d           0    0    department_dept_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.department_dept_id_seq OWNED BY public.department.dept_id;
          public          postgres    false    218            �            1259    17087    employee    TABLE     �  CREATE TABLE public.employee (
    emp_id integer NOT NULL,
    f_name character varying(255) NOT NULL,
    l_name character varying(255) NOT NULL,
    gender character(1) NOT NULL,
    age smallint NOT NULL,
    address character varying(255) NOT NULL,
    phone_num character varying(50) NOT NULL,
    email character varying(255) NOT NULL,
    emp_type character varying(255) NOT NULL,
    title character varying(255) NOT NULL,
    dept_id integer
);
    DROP TABLE public.employee;
       public         heap    postgres    false            �            1259    17092    employee_emp_id_seq    SEQUENCE     �   CREATE SEQUENCE public.employee_emp_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.employee_emp_id_seq;
       public          postgres    false    219            e           0    0    employee_emp_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.employee_emp_id_seq OWNED BY public.employee.emp_id;
          public          postgres    false    220            �            1259    17093    hospital    TABLE     �   CREATE TABLE public.hospital (
    hospital_id integer NOT NULL,
    hospital_name character varying(255) NOT NULL,
    address character varying(255) NOT NULL,
    phone_num character varying(50) NOT NULL
);
    DROP TABLE public.hospital;
       public         heap    postgres    false            �            1259    17098    medical_record    TABLE       CREATE TABLE public.medical_record (
    record_id integer NOT NULL,
    pat_id integer,
    emp_id integer,
    symptoms text,
    diag_id character varying(255),
    record_procedures text,
    notes text,
    created timestamp with time zone NOT NULL
);
 "   DROP TABLE public.medical_record;
       public         heap    postgres    false            �            1259    17103    medical_record_record_id_seq    SEQUENCE     �   CREATE SEQUENCE public.medical_record_record_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.medical_record_record_id_seq;
       public          postgres    false    222            f           0    0    medical_record_record_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.medical_record_record_id_seq OWNED BY public.medical_record.record_id;
          public          postgres    false    223            �            1259    17104    patient    TABLE       CREATE TABLE public.patient (
    pat_id integer NOT NULL,
    f_name character varying(255),
    l_name character varying(255),
    gender character(1),
    age smallint,
    address character varying(255),
    phone_num character varying(50),
    ssn character varying(20) NOT NULL
);
    DROP TABLE public.patient;
       public         heap    postgres    false            �            1259    17109    patient_pat_id_seq    SEQUENCE     �   CREATE SEQUENCE public.patient_pat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.patient_pat_id_seq;
       public          postgres    false    224            g           0    0    patient_pat_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.patient_pat_id_seq OWNED BY public.patient.pat_id;
          public          postgres    false    225            �            1259    17115    prescription    TABLE     �   CREATE TABLE public.prescription (
    presc_id integer NOT NULL,
    record_id integer,
    instructions text NOT NULL,
    created timestamp with time zone NOT NULL,
    medication text
);
     DROP TABLE public.prescription;
       public         heap    postgres    false            �            1259    17120    prescription_presc_id_seq    SEQUENCE     �   CREATE SEQUENCE public.prescription_presc_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.prescription_presc_id_seq;
       public          postgres    false    226            h           0    0    prescription_presc_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.prescription_presc_id_seq OWNED BY public.prescription.presc_id;
          public          postgres    false    227            �            1259    17121    room    TABLE     P   CREATE TABLE public.room (
    room_id integer NOT NULL,
    bldg_id integer
);
    DROP TABLE public.room;
       public         heap    postgres    false            �            1259    17124    room_room_id_seq    SEQUENCE     �   CREATE SEQUENCE public.room_room_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.room_room_id_seq;
       public          postgres    false    228            i           0    0    room_room_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.room_room_id_seq OWNED BY public.room.room_id;
          public          postgres    false    229            �            1259    17125    users    TABLE     �   CREATE TABLE public.users (
    emp_id integer NOT NULL,
    email character varying(255) NOT NULL,
    passwd character varying(255) NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            �           2604    17130    building bldg_id    DEFAULT     t   ALTER TABLE ONLY public.building ALTER COLUMN bldg_id SET DEFAULT nextval('public.building_bldg_id_seq'::regclass);
 ?   ALTER TABLE public.building ALTER COLUMN bldg_id DROP DEFAULT;
       public          postgres    false    216    215            �           2604    17131    department dept_id    DEFAULT     x   ALTER TABLE ONLY public.department ALTER COLUMN dept_id SET DEFAULT nextval('public.department_dept_id_seq'::regclass);
 A   ALTER TABLE public.department ALTER COLUMN dept_id DROP DEFAULT;
       public          postgres    false    218    217            �           2604    17132    employee emp_id    DEFAULT     r   ALTER TABLE ONLY public.employee ALTER COLUMN emp_id SET DEFAULT nextval('public.employee_emp_id_seq'::regclass);
 >   ALTER TABLE public.employee ALTER COLUMN emp_id DROP DEFAULT;
       public          postgres    false    220    219            �           2604    17133    medical_record record_id    DEFAULT     �   ALTER TABLE ONLY public.medical_record ALTER COLUMN record_id SET DEFAULT nextval('public.medical_record_record_id_seq'::regclass);
 G   ALTER TABLE public.medical_record ALTER COLUMN record_id DROP DEFAULT;
       public          postgres    false    223    222            �           2604    17134    patient pat_id    DEFAULT     p   ALTER TABLE ONLY public.patient ALTER COLUMN pat_id SET DEFAULT nextval('public.patient_pat_id_seq'::regclass);
 =   ALTER TABLE public.patient ALTER COLUMN pat_id DROP DEFAULT;
       public          postgres    false    225    224            �           2604    17135    prescription presc_id    DEFAULT     ~   ALTER TABLE ONLY public.prescription ALTER COLUMN presc_id SET DEFAULT nextval('public.prescription_presc_id_seq'::regclass);
 D   ALTER TABLE public.prescription ALTER COLUMN presc_id DROP DEFAULT;
       public          postgres    false    227    226            �           2604    17136    room room_id    DEFAULT     l   ALTER TABLE ONLY public.room ALTER COLUMN room_id SET DEFAULT nextval('public.room_room_id_seq'::regclass);
 ;   ALTER TABLE public.room ALTER COLUMN room_id DROP DEFAULT;
       public          postgres    false    229    228            L          0    17073    appointment 
   TABLE DATA           i   COPY public.appointment (pat_id, start_time, emp_id, room_id, end_time, status, cancel_rson) FROM stdin;
    public          postgres    false    214   :_       M          0    17079    building 
   TABLE DATA           F   COPY public.building (bldg_id, bldg_address, hospital_id) FROM stdin;
    public          postgres    false    215   �_       O          0    17083 
   department 
   TABLE DATA           E   COPY public.department (dept_id, dept_name, hospital_id) FROM stdin;
    public          postgres    false    217   �_       Q          0    17087    employee 
   TABLE DATA           |   COPY public.employee (emp_id, f_name, l_name, gender, age, address, phone_num, email, emp_type, title, dept_id) FROM stdin;
    public          postgres    false    219   �`       S          0    17093    hospital 
   TABLE DATA           R   COPY public.hospital (hospital_id, hospital_name, address, phone_num) FROM stdin;
    public          postgres    false    221   #b       T          0    17098    medical_record 
   TABLE DATA           y   COPY public.medical_record (record_id, pat_id, emp_id, symptoms, diag_id, record_procedures, notes, created) FROM stdin;
    public          postgres    false    222   qb       V          0    17104    patient 
   TABLE DATA           _   COPY public.patient (pat_id, f_name, l_name, gender, age, address, phone_num, ssn) FROM stdin;
    public          postgres    false    224   8e       X          0    17115    prescription 
   TABLE DATA           ^   COPY public.prescription (presc_id, record_id, instructions, created, medication) FROM stdin;
    public          postgres    false    226   -f       Z          0    17121    room 
   TABLE DATA           0   COPY public.room (room_id, bldg_id) FROM stdin;
    public          postgres    false    228   �f       \          0    17125    users 
   TABLE DATA           6   COPY public.users (emp_id, email, passwd) FROM stdin;
    public          postgres    false    230   g       j           0    0    building_bldg_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.building_bldg_id_seq', 3, true);
          public          postgres    false    216            k           0    0    department_dept_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.department_dept_id_seq', 15, true);
          public          postgres    false    218            l           0    0    employee_emp_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.employee_emp_id_seq', 8, true);
          public          postgres    false    220            m           0    0    medical_record_record_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.medical_record_record_id_seq', 6, true);
          public          postgres    false    223            n           0    0    patient_pat_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.patient_pat_id_seq', 8, true);
          public          postgres    false    225            o           0    0    prescription_presc_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.prescription_presc_id_seq', 1, true);
          public          postgres    false    227            p           0    0    room_room_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.room_room_id_seq', 30, true);
          public          postgres    false    229            �           2606    17138    appointment appointment_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_pkey PRIMARY KEY (pat_id, start_time);
 F   ALTER TABLE ONLY public.appointment DROP CONSTRAINT appointment_pkey;
       public            postgres    false    214    214            �           2606    17140    building building_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.building
    ADD CONSTRAINT building_pkey PRIMARY KEY (bldg_id);
 @   ALTER TABLE ONLY public.building DROP CONSTRAINT building_pkey;
       public            postgres    false    215            �           2606    17141    appointment check_status    CHECK CONSTRAINT     �   ALTER TABLE public.appointment
    ADD CONSTRAINT check_status CHECK ((status = ANY (ARRAY['A'::bpchar, 'C'::bpchar]))) NOT VALID;
 =   ALTER TABLE public.appointment DROP CONSTRAINT check_status;
       public          postgres    false    214    214            �           2606    17143    department department_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (dept_id);
 D   ALTER TABLE ONLY public.department DROP CONSTRAINT department_pkey;
       public            postgres    false    217            �           2606    17145    employee employee_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (emp_id);
 @   ALTER TABLE ONLY public.employee DROP CONSTRAINT employee_pkey;
       public            postgres    false    219            �           2606    17147    hospital hospital_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.hospital
    ADD CONSTRAINT hospital_pkey PRIMARY KEY (hospital_id);
 @   ALTER TABLE ONLY public.hospital DROP CONSTRAINT hospital_pkey;
       public            postgres    false    221            �           2606    17149 "   medical_record medical_record_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY public.medical_record
    ADD CONSTRAINT medical_record_pkey PRIMARY KEY (record_id);
 L   ALTER TABLE ONLY public.medical_record DROP CONSTRAINT medical_record_pkey;
       public            postgres    false    222            �           2606    17151    patient patient_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.patient
    ADD CONSTRAINT patient_pkey PRIMARY KEY (pat_id);
 >   ALTER TABLE ONLY public.patient DROP CONSTRAINT patient_pkey;
       public            postgres    false    224            �           2606    17155    prescription prescription_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.prescription
    ADD CONSTRAINT prescription_pkey PRIMARY KEY (presc_id);
 H   ALTER TABLE ONLY public.prescription DROP CONSTRAINT prescription_pkey;
       public            postgres    false    226            �           2606    17157    room room_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_pkey PRIMARY KEY (room_id);
 8   ALTER TABLE ONLY public.room DROP CONSTRAINT room_pkey;
       public            postgres    false    228            �           2606    17159    employee unique_email 
   CONSTRAINT     Q   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT unique_email UNIQUE (email);
 ?   ALTER TABLE ONLY public.employee DROP CONSTRAINT unique_email;
       public            postgres    false    219            �           2606    17161    patient unique_ssn 
   CONSTRAINT     L   ALTER TABLE ONLY public.patient
    ADD CONSTRAINT unique_ssn UNIQUE (ssn);
 <   ALTER TABLE ONLY public.patient DROP CONSTRAINT unique_ssn;
       public            postgres    false    224            �           2606    17163    users users_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (emp_id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    230            �           1259    17230 	   idx_email    INDEX     <   CREATE INDEX idx_email ON public.users USING btree (email);
    DROP INDEX public.idx_email;
       public            postgres    false    230            �           1259    17229    idx_start_time    INDEX     L   CREATE INDEX idx_start_time ON public.appointment USING btree (start_time);
 "   DROP INDEX public.idx_start_time;
       public            postgres    false    214            �           2606    17164 #   appointment appointment_emp_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_emp_id_fkey FOREIGN KEY (emp_id) REFERENCES public.employee(emp_id) ON UPDATE CASCADE;
 M   ALTER TABLE ONLY public.appointment DROP CONSTRAINT appointment_emp_id_fkey;
       public          postgres    false    214    3232    219            �           2606    17169 #   appointment appointment_pat_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_pat_id_fkey FOREIGN KEY (pat_id) REFERENCES public.patient(pat_id) ON UPDATE CASCADE;
 M   ALTER TABLE ONLY public.appointment DROP CONSTRAINT appointment_pat_id_fkey;
       public          postgres    false    214    3240    224            �           2606    17174 $   appointment appointment_room_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_room_id_fkey FOREIGN KEY (room_id) REFERENCES public.room(room_id) ON UPDATE CASCADE;
 N   ALTER TABLE ONLY public.appointment DROP CONSTRAINT appointment_room_id_fkey;
       public          postgres    false    214    3246    228            �           2606    17179 "   building building_hospital_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.building
    ADD CONSTRAINT building_hospital_id_fkey FOREIGN KEY (hospital_id) REFERENCES public.hospital(hospital_id) ON UPDATE CASCADE;
 L   ALTER TABLE ONLY public.building DROP CONSTRAINT building_hospital_id_fkey;
       public          postgres    false    221    3236    215            �           2606    17184 &   department department_hospital_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_hospital_id_fkey FOREIGN KEY (hospital_id) REFERENCES public.hospital(hospital_id) ON UPDATE CASCADE;
 P   ALTER TABLE ONLY public.department DROP CONSTRAINT department_hospital_id_fkey;
       public          postgres    false    217    221    3236            �           2606    17189    employee employee_dept_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_dept_id_fkey FOREIGN KEY (dept_id) REFERENCES public.department(dept_id) ON UPDATE CASCADE;
 H   ALTER TABLE ONLY public.employee DROP CONSTRAINT employee_dept_id_fkey;
       public          postgres    false    219    217    3230            �           2606    17199 !   prescription presc_record_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.prescription
    ADD CONSTRAINT presc_record_id_fkey FOREIGN KEY (record_id) REFERENCES public.medical_record(record_id) NOT VALID;
 K   ALTER TABLE ONLY public.prescription DROP CONSTRAINT presc_record_id_fkey;
       public          postgres    false    226    3238    222            �           2606    17204 !   medical_record record_emp_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.medical_record
    ADD CONSTRAINT record_emp_id_fkey FOREIGN KEY (emp_id) REFERENCES public.employee(emp_id) NOT VALID;
 K   ALTER TABLE ONLY public.medical_record DROP CONSTRAINT record_emp_id_fkey;
       public          postgres    false    222    3232    219            �           2606    17209 !   medical_record record_pat_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.medical_record
    ADD CONSTRAINT record_pat_id_fkey FOREIGN KEY (pat_id) REFERENCES public.patient(pat_id) NOT VALID;
 K   ALTER TABLE ONLY public.medical_record DROP CONSTRAINT record_pat_id_fkey;
       public          postgres    false    3240    224    222            �           2606    17214    room room_bldg_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_bldg_id_fkey FOREIGN KEY (bldg_id) REFERENCES public.building(bldg_id) ON UPDATE CASCADE;
 @   ALTER TABLE ONLY public.room DROP CONSTRAINT room_bldg_id_fkey;
       public          postgres    false    3228    215    228            �           2606    17219    users users_email_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_fkey FOREIGN KEY (email) REFERENCES public.employee(email) NOT VALID;
 @   ALTER TABLE ONLY public.users DROP CONSTRAINT users_email_fkey;
       public          postgres    false    3234    219    230            �           2606    17224    users users_emp_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_emp_id_fkey FOREIGN KEY (emp_id) REFERENCES public.employee(emp_id) ON UPDATE CASCADE;
 A   ALTER TABLE ONLY public.users DROP CONSTRAINT users_emp_id_fkey;
       public          postgres    false    219    3232    230            L   u   x�]α� �������@�s'p�9�T|���0�8?aK�%���@�H{��\��G�8!(U��3��\��ެ%���ȗ|C�Ǫh#�Y�/I�v���1��N%�k���3�      M      x�3�4t�4�2�4tRƜ��@*F��� 1      O   �   x�U��
�0E�ӯ�����R����܄8��4LR�oR��.9�ܛ(�0:_���n�T2�k'%]�[�Z|���C��Iڤw�2(j�A�U�������P��_\8�G|�!�@�p�N��
��tV{j�w�P���vJ�l��o�)\��	���j�.r�﬚�Y|�����������6��2�9�{F3��$I޸�^      Q   M  x���OK�0��o>E�G!��Y���Tt�Ý��&k#Y�I*��͚Z��C �ϓ���@C���Vj�84��a�pkWyY'$M�t<)B�1~-i����J����p����e���NHy�j.Ȃ ��}���J�N���h�;aT(�����U7�灟O�lh1;&/ß8��
�^���O`�,��'��/����G1;/�D��#�X@�Ug{�b�X�b��ş����0��P�*x�KJ{��q��WQQE5Q�1�-���`:�d��5UǞ�du�APOk�A�ҹtb���
X�^���,��@.�d����x�%z��|��      S   >   x�3��I�(�T��/.�,I��t�I�.N�+I-���N,)U0��66�P0�T0130����� �5�      T   �  x���Mo�H�ϓ_�{eA�c�7'�a�6�^�#��u>���;J���Ȓ!͐|����Y����x�9WOct1Q�B쥘��fۯ�1�;'iRK��ѳy�E�*4Vm��N��f�@N��NZX�+#�t�\�PR�Q����jخ�w4.׻as�1[���J`��-E>K�����?��r��sL�Y���(��4����1RЬ�
ؚ�<V��_"PLV�!����$�:��yJ,0�GE|�M�2A0�}�0���7�����M�%�3WR����3�k�ޢ�X��rs)xp��|tMn�fJ|ґ�n�^�[Z��1���,/�Zv�_���Y�w���?����Z÷���P���e���'ly��%I����S��ppF-][a-~��q�v����Ñ2�*���ߖ�b�T]IjU@�54�@sM5�אܙ;4�CM|�R�&y��ZBm{�8IO�����D�ͱB��� �}����n���a���O�J⸠^����b�t��u%!o!ܩ�Ԏj�t��U�u��=kX��x���܂��z��S�e$�F$v�q.4c����	�q,ZmņCV�A�u��֔@�7K���'��{�7P��b9�*d�E�A˰��)qi��m����3"V�L�;����՝�bU��E���o5��/S��D�9�Ul_����� ����      V   �   x�}�=k�0���_a�(�%�!�Х��X$E�)u}�u�j8nz�����qx=y紵�:�t�E����/��|T	VqQ7Cj�*�h���M���:��$�M���8�S���2��$�v���6��b��m$��ik��W��`�h~t�Jj���\f֚�]��k�"�;I-��E]�j�F�sJo��]gp/���9)��VVǔ]-ob����%����,q3      X   }   x�u�;
�0�zu�-��>��!r7�-���
�n�X�5L9oƀ����#g��c*-s~���-�-�Z?gn�I�0�]9X_@�Ɓ%c#	��qF���$,x9��9b����O��}�1�zWJ}��1�      Z   F   x��� 1�7�e��8�8v�!����LY��ȕ��IE�m:t�U
+Ϥ�I�6�Ԫ�z���W��      \   J  x���K��@ D�pvt𑏰0b�EED��M��
(
(���WhO�2#_���H��1�Ӏr�\�IG�p9�0�]��y�D�A+UQ$�k\I_�Jf,GȌ	�f�/^Dحp�J��ݨ\�=���0���$g��Ʈ���<��ۦT���M�@��X�?%�|Vu4O��C�7�y��{ʂ\��l��6�9߬��ٓ�����\�*�����t�s�����^�\?��k__��ֳ��3�(o�6]lF��=/Fպ;�<iK�=�@^*)	�@�e��e˥��k'9�.nz\�l} ig�0i�T��BC�B�]˳>����f���^��gy����~���'�C}$��a�`���t��o��Yn�p죗�9Ůc+]txK�6֮| r1���V)��)!����0�j}��]Y����/ݱ`�����4�������BCu!JB9D�ʹ��`� Pr|&a�$��4]��>%�i;$SV�Q�x;z���j��\q�N�򥾆��~�}�gZ�*�f�IP��q�ߎD�$OQ�(��$��yj�@&���3���؂�U+���P���(j�F��h��"Px     