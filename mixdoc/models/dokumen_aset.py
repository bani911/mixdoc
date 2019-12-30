# -*- coding: utf-8 -*-
# Dokumen ASET

from odoo import models, fields, api

class dokumen_aset(models.Model):
    _name = 'dokumen.aset'

    contact_person = fields.Many2one('res.users', 'PIC', domain="[('active','=','t')]")
    company_id = fields.Many2one('res.company', 'Organisasi', default=lambda self: self.env.user.company_id, readonly=True)
    jenis_dokumen = fields.Many2one('jenis.dokumen', 'Jenis Dokumen')
    nama = fields.Char(string="Nama Dokumen", required=True)
    no_eksternal = fields.Char(string="No.Fisik Dokumen", required=True)
    perihal = fields.Char(string="Perihal", required=True)
    # tgl_terbit = fields.Date('Tgl Terbit')
    # tgl_expired = fields.Date('Tgl Expired')
    lampiran_dokumen = fields.Binary("Lampiran_1")
    doc_filename_dokumen = fields.Char("Filename Lampiran 1")
    lampiran_dokumen2 = fields.Binary("Lampiran_2")
    doc_filename_dokumen2 = fields.Char("Filename Lampiran 2")
    lampiran_dokumen3 = fields.Binary("Lampiran_3")
    doc_filename_dokumen3 = fields.Char("Filename Lampiran 3")
    # is_valid = fields.Boolean('is Valid?')
    keterangan = fields.Text('Keterangan')
    kuasa_fisik = fields.Many2one('kuasa.fisik', 'Penguasaan Fisik')
    luas = fields.Integer(string="Luas (M2)")
    atas_nama = fields.Char(string="Atas Nama")
    nilai_perolehan = fields.Float('Nilai Perolehan (Rp.)')
    notaris = fields.Char(string="Notaris")
    tempat_simpan = fields.Many2one('tempat.simpan', 'Penyimpanan')
    ket_simpan = fields.Char("Keterangan Simpan")
    jenis_unit = fields.Many2one('jenis.unit', 'Tipe Organisasi')
    bagian = fields.Many2one('bagian', 'Bagian', domain="[('ju', '=', jenis_unit)]")
    # penerbit = fields.Many2one('res.users', 'Penerbit', domain="[('active','=','t')]")

    _sql_constraints = [('cek_unik_nomor', 'UNIQUE(no_eksternal)', 'No.Fisik Dokumen tidak boleh sama!')]