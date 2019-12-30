# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import datetime

class surat_keluar(models.Model):
    _name = 'surat.keluar'

    company_id = fields.Many2one('res.company', 'Organisasi', default=lambda self: self.env.user.company_id, readonly=True)
    no_surat = fields.Char(string="No. Surat", readonly=True)
    contact_person = fields.Many2one('res.users', 'PIC')
    tipe_org = fields.Many2one('jenis.unit', 'Tipe_Org', required=True)
    jenis_surat = fields.Many2one('jenis.surat', 'Jns_Surat', domain="[('kalangan', '=', kalangan)]")
    kalangan = fields.Many2one('kalangan.surat', 'Kategori')
    # macam_surat = fields.Many2one('macam.surat', 'Macam Surat', domain="[('id','=',2)]")
    perihal = fields.Char(string="Perihal", required=True)
    tgl_surat = fields.Date('Tgl Surat', required=True)
    tgl_kirim = fields.Date('Tgl Kirim', required=True)
    # isi = fields.Text('Isi')
    keterangan = fields.Text('Keterangan')
    lampiran_keluar = fields.Binary("Lampiran_1")
    doc_filename_keluar = fields.Char("Filename Lampiran 1")
    lampiran_keluar2 = fields.Binary("Lampiran_2")
    doc_filename_keluar2 = fields.Char("Filename Lampiran 2")
    lampiran_keluar3 = fields.Binary("Lampiran_3")
    doc_filename_keluar3 = fields.Char("Filename Lampiran 3")
    bagian = fields.Many2one('bagian', 'Bagian', domain="[('tipe_org', '=', tipe_org)]")
    jabminta = fields.Many2one('res.users', 'Yg_Meminta')
    jabttd = fields.Many2one('res.users', 'Penandatangan')
    bag_minta = fields.Many2one('bagian', 'Bagian_yang_Meminta')
    ref_surat_masuk = fields.Many2one('surat.masuk', 'Ref_Surat_Masuk')
    disposisi_status = fields.Many2one('disposisi.status.keluar', 'Metode Pengiriman')
    tempat_simpan = fields.Many2one('tempat.simpan', 'Penyimpanan')
    ket_simpan = fields.Char("Ket_Simpan")
    # jenis_perusahaan = fields.Many2one('jenis.perusahaan', 'Jenis Perusahaan', required=True)
    is_eksternal = fields.Boolean('is_Eksternal?')
    penerima = fields.Many2one('res.users', 'Penerima_Internal')
    penerima_eksternal = fields.Many2one('penerima.eksternal', 'Penerima_Eksternal')
    org_penerima = fields.Char("Organisasi_Penerima")
    org_penerima_eksternal = fields.Many2one('org.penerima.eksternal', 'Org_Penerima_Eksternal')


    def get_sequence(self, name=False, obj=False, pref=False, context=None):
        sequence_id = self.env['ir.sequence'].search([('name', '=', name), ('code', '=', obj), ('prefix', '=', pref)])
        if not sequence_id:
            sequence_id = self.env['ir.sequence'].sudo().create({
                'name': name,
                'code': obj,
                'implementation': 'no_gap',
                'prefix': '',
                'padding': 3
            })
        return sequence_id.next_by_id()

    @api.model
    def create(self, vals):
        # get bagian kode
        tbl_bagian = self.env['bagian']
        b = tbl_bagian.search([("id","=", vals['bagian'])])
        # get jenis_surat kode
        tbl_jns_surat = self.env['jenis.surat']
        c = tbl_jns_surat.search([("id","=", vals['jenis_surat'])])
        # get jenis_perusahaan
        # tbl_jns_perusahaan = self.env['jenis.perusahaan']
        # d = tbl_jns_perusahaan.search([("id","=", vals['jenis_perusahaan'])])
        # get tipe_organisasi
        tbl_jns_unit = self.env['jenis.unit']
        e = tbl_jns_unit.search([("id","=", vals['tipe_org'])])
        # get kode organisasi session
        kode = self.env.user.company_id.kode
        # kode = self.env.user.company_id.kode_organisasi
        a = self.get_sequence('Kode Nomor Surat Keluar', 'surat.keluar','')

        vals['no_surat'] = kode + '-' + e[0].kode + '/O/' + b[0].singkatan + '-' + c[0].kode + '/' + datetime.date.today().strftime("%m") + '-' + datetime.date.today().strftime("%Y") + '/' + a
        return super(surat_keluar, self).create(vals)