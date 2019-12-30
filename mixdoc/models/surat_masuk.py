# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class surat_masuk(models.Model):
    _name = 'surat.masuk'

    company_id = fields.Many2one('res.company', 'Organisasi', default=lambda self: self.env.user.company_id, readonly=True)
    # no_surat = fields.Char(string="No. Surat", readonly=True)
    contact_person = fields.Many2one('res.users', 'PIC', domain="[('active','=','t')]")
    pengirim = fields.Char(string="Pengirim", required=True)
    jenis_surat = fields.Many2one('jenis.surat', 'Jenis Surat', domain="[('kalangan', '=', kalangan)]")
    kalangan = fields.Many2one('kalangan.surat', 'Kategori')
    # disposisi = fields.Many2one('disposisi', 'Disposisi')
    tipe_org = fields.Many2one('jenis.unit', 'Tipe_Org', required=True)
    status = fields.Many2one('status.surat', 'Status')
    # macam_surat = fields.Many2one('macam.surat', 'Macam Surat', domain="[('id','=',1)]")
    alamat = fields.Text('Alamat')
    no_eksternal = fields.Char(string="No.Surat", required=True)
    tgl_surat = fields.Date('Tgl Surat')
    tgl_terima = fields.Date('Tgl_Diterima')
    perihal = fields.Char(string="Perihal")
    keterangan = fields.Text('Keterangan')
    lampiran_masuk = fields.Binary("Lampiran_1")
    doc_filename_masuk = fields.Char("Filename Lampiran 1")
    lampiran_masuk2 = fields.Binary("Lampiran_2")
    doc_filename_masuk2 = fields.Char("Filename Lampiran 2")
    bagian = fields.Many2one('bagian', 'Bagian', domain="[('tipe_org', '=', tipe_org)]")
    penerima = fields.Many2one('res.users', 'Penerima')
    tempat_simpan = fields.Many2one('tempat.simpan', 'Penyimpanan')
    ket_simpan = fields.Char("Ket.Simpan")

    _sql_constraints = [('cek_unik_nomor', 'UNIQUE(no_eksternal)', 'No.Surat Eksternal tidak boleh sama!')]

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, rec.no_eksternal))
        return res